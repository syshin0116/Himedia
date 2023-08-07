package com.apple.planner;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity3 extends AppCompatActivity {
    Button button;
    WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        button = findViewById(R.id.button);
        webView = findViewById(R.id.webview);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(getApplicationContext(),
                        "웹사이트로 이동",
                        Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(Intent.ACTION_VIEW,
                        Uri.parse("http://ec2-3-34-145-18.ap-northeast-2.compute.amazonaws.com:8080/trip/main.jsp"));
                startActivity(intent);
            }//onclick
        });//button
        webView.setWebViewClient(new TripClient());
        // webView에 url을 끼워넣어줄 객체를 하나 지정
        // url을 끼워넣어주는 객체를 WebviewClient
        // 사이트를 액티비티에 끼워넣었을 떄
        // 여러 설정을 따로 해주어야 한다.
        // 여러 설정만을 담당하는 객체를 사용한다.
        WebSettings webSet = webView.getSettings();

        webSet.setBuiltInZoomControls(true);
        webSet.setJavaScriptEnabled(true);
        webSet.setAllowContentAccess(true);
        webSet.setAppCacheEnabled(true);
        webSet.setDomStorageEnabled(true);
        webSet.setUseWideViewPort(true);
        webSet.setAllowFileAccess(true);
        webSet.setAllowFileAccessFromFileURLs(true);
        webView.loadUrl("http://ec2-3-34-145-18.ap-northeast-2.compute.amazonaws.com:8080/trip/main.jsp");
    }
}

class TripClient extends WebViewClient{
    // 오버라이드

    @Override
    public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
        return super.shouldOverrideUrlLoading(view, request);
    }
}
