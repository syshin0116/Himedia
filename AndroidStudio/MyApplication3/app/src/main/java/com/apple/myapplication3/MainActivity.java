package com.apple.myapplication3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // view 객체의 값을 넣어줄 변수를 선언!!
    Button b1, b2;
    TextView t1, t2;


    @Override

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 안드로이드에서는 자원과 관련된 것은 R 클래스가 담당하고 값이 저장된 변수를 가지고 잇음
        // R 클래스가 가지고 잇는 변수를 가지고 view객체에 대한 주소를 획득하여 선언된 변수에 저장
        b1 = findViewById(R.id.button2);
        b2 = findViewById(R.id.button3);
        t1 = findViewById(R.id.t1);
        t2 = findViewById(R.id.t2);

        // b1에 클릭 이벤트를 등록
        // 인터페이스를 따르는 익명클래스의 객체를 입력값으로 넣어줌
        // 이 생성된 객체가 이벤트를 담당
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 처리내용!! 을 구현
                Log.d("확인용", "버튼1");
                String s1 = t1.getText().toString();
                Log.d("입력값", s1);
            }
        });//b1
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.d("확인용", "버튼2");
                String s2 = t2.getText().toString();
                Log.d("입력값", s2);
            }
        });
//        t1.setTextColor("@color/red");
//        t2.setTextColor("blue");


    }


}