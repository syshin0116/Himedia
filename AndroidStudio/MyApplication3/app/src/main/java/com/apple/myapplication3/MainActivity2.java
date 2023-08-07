package com.apple.myapplication3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class MainActivity2 extends AppCompatActivity {

    Button b4, b5;


    @Override

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        b4 = findViewById(R.id.button4);
        b5 = findViewById(R.id.button5);
        // b1에 클릭 이벤트를 등록
        // 인터페이스를 따르는 익명클래스의 객체를 입력값으로 넣어줌
        // 이 생성된 객체가 이벤트를 담당
        b4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 처리내용!! 을 구현
                Log.d("확인용", "버튼1");
            }
        });//b1
        b5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });
    }


}