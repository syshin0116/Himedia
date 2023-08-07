package com.apple.myapplication3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;

import com.google.android.material.textfield.TextInputLayout;

import org.w3c.dom.Text;

public class calculator extends AppCompatActivity {

    ImageButton b_add, b_subtract, b_multiply, b_divide, b_equal, b_reset;
    EditText num1, num2;
    TextView result;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);

        b_reset = findViewById(R.id.resetButton);
        b_add = findViewById(R.id.imageButton);
        b_subtract = findViewById(R.id.imageButton2);
        b_multiply = findViewById(R.id.imageButton3);
        b_divide = findViewById(R.id.imageButton4);
        num1 = findViewById(R.id.num1);
        num2 = findViewById(R.id.num2);
        result = findViewById(R.id.result);


        b_add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                String s1 = num1.getText().toString();
//                String s2 = num2.getText().toString();
//
//                int i1 = Integer.parseInt(s1);
//                int i2 = Integer.parseInt(s2);
//
//                int sum = i1+i2;
                int[] datas = input();
                int calc = datas[0] + datas[1];
                result.setText("결과는 " + calc);
            }
        });
        b_subtract.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int[] datas = input();
                int calc = datas[0] - datas[1];
                result.setText("결과는 " + calc);
            }
        });

        b_multiply.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int[] datas = input();
                int calc = datas[0] * datas[1];
                result.setText("결과는 " + calc);
            }
        });

        b_divide.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int[] datas = input();
                int calc = datas[0] / datas[1];
                result.setText("결과는 " + calc);
            }
        });
    }
        public int[] input(){
            //데이터를 가지고 와서,
            String s11 = num1.getText().toString();
            String s22 = num2.getText().toString();

            //정수로 변경하고
            int i11 = Integer.parseInt(s11);
            int i22 = Integer.parseInt(s22);

            int[] values = new int[2];
            values[0] = i11;
            values[1] = i22;
            return values;
    }
}