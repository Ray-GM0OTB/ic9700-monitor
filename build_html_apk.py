"""
Builds an offline Android app (APK) from a single HTML page.  by GM0OTB

    py build_html_apk.py "Connector Cross-Reference.html" "Connector X-Ref"

The page is packed inside the app, so it works with no internet (web fonts load when online,
otherwise the page's own fallback fonts are used). Its Print buttons open Android's print
dialog (which also offers "Save as PDF"), and anything the page remembers (recent searches)
is kept between runs. Uses the same Java / Android SDK / signing key as build_apk.py, which
must be in the same folder.
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_apk as B                       # noqa: E402  (shared download / build / sign steps)

JAVA = r'''package __PACKAGE__;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.CancellationSignal;
import android.os.ParcelFileDescriptor;
import android.print.PageRange;
import android.print.PrintAttributes;
import android.print.PrintDocumentAdapter;
import android.print.PrintManager;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;

/** __TITLE__: an HTML page packed as an offline app (by GM0OTB). */
public class MainActivity extends Activity {
    // The page is loaded under this https address so it counts as a secure page (clipboard,
    // storage) - nothing is fetched from it; the page itself is inside the app.
    private static final String BASE = "https://__HOST__/";
    private WebView web;

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);
        web = new WebView(this);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setTextZoom(100);
        web.addJavascriptInterface(new Bridge(), "AppBridge");
        web.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                Uri u = request.getUrl();
                if ("__HOST__".equals(u.getHost())) {
                    return false;
                }
                try {
                    startActivity(new Intent(Intent.ACTION_VIEW, u));    // outside links open in the browser
                } catch (Exception e) {
                    // no browser
                }
                return true;
            }
        });
        setContentView(web);
        web.loadDataWithBaseURL(BASE, readPage(), "text/html", "utf-8", null);
    }

    private String readPage() {
        try {
            int id = getResources().getIdentifier("page", "raw", getPackageName());
            InputStream in = getResources().openRawResource(id);
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            byte[] buf = new byte[16384];
            int n;
            while ((n = in.read(buf)) > 0) {
                out.write(buf, 0, n);
            }
            in.close();
            return out.toString("UTF-8");
        } catch (Exception e) {
            return "<p>Page missing: " + e + "</p>";
        }
    }

    /** window.print() in the page comes here. */
    private class Bridge {
        @JavascriptInterface
        public void print(final String title) {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    doPrint(title == null || title.length() == 0 ? "__TITLE__" : title);
                }
            });
        }
    }

    private void doPrint(String title) {
        PrintManager pm = (PrintManager) getSystemService(Context.PRINT_SERVICE);
        final PrintDocumentAdapter inner = web.createPrintDocumentAdapter(title);
        PrintDocumentAdapter wrap = new PrintDocumentAdapter() {
            @Override
            public void onStart() {
                inner.onStart();
            }

            @Override
            public void onLayout(PrintAttributes oldA, PrintAttributes newA, CancellationSignal cancel,
                                 LayoutResultCallback cb, Bundle extras) {
                inner.onLayout(oldA, newA, cancel, cb, extras);
            }

            @Override
            public void onWrite(PageRange[] pages, ParcelFileDescriptor dest, CancellationSignal cancel,
                                WriteResultCallback cb) {
                inner.onWrite(pages, dest, cancel, cb);
            }

            @Override
            public void onFinish() {
                inner.onFinish();
                web.evaluateJavascript("dispatchEvent(new Event('afterprint'))", null);   // page tidies up
            }
        };
        pm.print(title, wrap, null);
    }

    @Override
    public void onBackPressed() {
        if (web != null && web.canGoBack()) {
            web.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onDestroy() {
        if (web != null) {
            web.destroy();
            web = null;
        }
        super.onDestroy();
    }
}
'''

MANIFEST = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="%s">
    <uses-permission android:name="android.permission.INTERNET"/>
    <application android:label="%s" android:icon="@mipmap/ic_launcher" android:allowBackup="true"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity" android:exported="true"
            android:configChanges="orientation|screenSize|screenLayout|smallestScreenSize|keyboard|keyboardHidden|uiMode|navigation">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
    </application>
</manifest>
"""

# Light on older phones; follows the phone's light / dark setting on Android 10 and later
STYLES = """<?xml version="1.0" encoding="utf-8"?>
<resources><style name="AppTheme" parent="@android:style/%s">
    <item name="android:windowNoTitle">true</item><item name="android:windowActionBar">false</item>
    <item name="android:statusBarColor">#14263b</item><item name="android:navigationBarColor">#14263b</item>
</style></resources>
"""

# window.print() goes to Android's print dialog (the page waits for 'beforeprint' / 'afterprint')
PRINT_SHIM = ("<script>window.print=function(){try{dispatchEvent(new Event('beforeprint'))}catch(e){}"
              "if(window.AppBridge)AppBridge.print(document.title||'')};</script>")


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "", text.lower())
    return (s or "page")[:30] if not s[:1].isdigit() else "p" + s[:29]


def write_sources(html_path, name, pkg, host):
    B.say("[3/5] App sources")
    shutil.rmtree(B.BUILD, ignore_errors=True)
    src = os.path.join(B.BUILD, "src", *pkg.split("."))
    os.makedirs(src)
    java = JAVA.replace("__PACKAGE__", pkg).replace("__TITLE__", name.replace('"', "'")).replace("__HOST__", host)
    with open(os.path.join(src, "MainActivity.java"), "w", encoding="utf-8") as f:
        f.write(java)
    esc = name.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")
    with open(os.path.join(B.BUILD, "AndroidManifest.xml"), "w", encoding="utf-8") as f:
        f.write(MANIFEST % (pkg, esc))
    res = os.path.join(B.BUILD, "res")
    for folder, parent in (("values", "Theme.Material.Light.NoActionBar"), ("values-v29", "Theme.DeviceDefault.DayNight")):
        os.makedirs(os.path.join(res, folder))
        with open(os.path.join(res, folder, "styles.xml"), "w", encoding="utf-8") as f:
            f.write(STYLES % parent)
    # the page itself
    with open(html_path, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()
    m = re.search(r"<head[^>]*>", html, re.I)
    html = html[:m.end()] + PRINT_SHIM + html[m.end():] if m else PRINT_SHIM + html
    os.makedirs(os.path.join(res, "raw"))
    with open(os.path.join(res, "raw", "page.html"), "w", encoding="utf-8") as f:
        f.write(html)
    B.say(f"  page: {os.path.basename(html_path)} ({len(html) // 1024} KB)")
    # icon: <page name>.png next to the page, else a built-in one
    icon_dir = os.path.join(res, "mipmap-xxxhdpi")
    os.makedirs(icon_dir)
    own = os.path.splitext(html_path)[0] + ".png"
    if os.path.exists(own):
        shutil.copy(own, os.path.join(icon_dir, "ic_launcher.png"))
        B.say(f"  icon: {os.path.basename(own)}")
    else:
        with open(os.path.join(icon_dir, "ic_launcher.png"), "wb") as f:
            f.write(B.png(192, (0xe0, 0x9a, 0x2b)))
        B.say(f"  icon: built-in (put {os.path.basename(own)} next to the page to use your own)")


def main():
    if len(sys.argv) < 2:
        B.fail('Usage: py build_html_apk.py "page.html" ["App name"]')
    html_path = os.path.abspath(sys.argv[1])
    if not os.path.exists(html_path):
        B.fail(f"{html_path} not found")
    name = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(os.path.basename(html_path))[0]
    sid = slug(name)
    pkg = "uk.gm0otb." + sid
    out_name = re.sub(r"[^A-Za-z0-9_-]+", "_", name).strip("_") + ".apk"
    # point the shared builder at this app
    B.LOG = os.path.join(HERE, "build_html_apk_log.txt")
    B.BUILD = os.path.join(B.SDK, "apk_build_" + sid)
    B.OUT_APK = os.path.join(os.path.dirname(html_path), out_name)
    try:
        os.remove(B.LOG)
    except OSError:
        pass
    B.say(f"{name} - offline Android app from {os.path.basename(html_path)} (GM0OTB)\n")
    jdk = B.ensure_jdk()
    B.ensure_sdk(jdk)
    write_sources(html_path, name, pkg, sid + ".app.local")
    aligned, env = B.build(jdk)
    B.sign(aligned, jdk, env)
    shutil.rmtree(B.BUILD, ignore_errors=True)
    B.say(f"\nDone: {B.OUT_APK}  ({os.path.getsize(B.OUT_APK) // 1024} KB)")
    B.say("Copy it to the phone, open it and allow 'install unknown apps' when asked. It works offline.")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except BaseException:
        import traceback
        B.say("\nUNEXPECTED ERROR:\n" + traceback.format_exc())
        sys.exit(1)
