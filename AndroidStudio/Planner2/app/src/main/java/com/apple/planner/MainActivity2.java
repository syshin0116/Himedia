package com.apple.planner;

import android.app.AlarmManager;
import android.app.DatePickerDialog;
import android.app.PendingIntent;
import android.app.TimePickerDialog;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TimePicker;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;



import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import java.util.Locale;

public class MainActivity2 extends AppCompatActivity {



    EditText alarmDateBack;
    EditText alarmClockBack;

    EditText name;
    Button add;
    Button cancel;
    String placeName;
    String placeDestination;
    Calendar myCalendar = Calendar.getInstance();
    Calendar currentCalendar = Calendar.getInstance();
    Calendar myCalendarRound = Calendar.getInstance();
    EditText alarmDate;
    EditText alarmClock;

    PendingIntent pendingIntent;
    PendingIntent pendingIntentRound;
    RadioButton single;
    RadioButton round;
    int years;
    int months;
    int days;
    public int hours = 2;
    public int minutes;
    int years2;
    int months2;
    int days2;
    public int hours2 = 2;
    public int minutes2;

    List<String> tripNames = new ArrayList<String>();
    String email;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        alarmClock = findViewById(R.id.editClock);
        alarmDate = (EditText) findViewById(R.id.editDate);
        alarmClockBack = findViewById(R.id.clockEdit_back);
        alarmDateBack = findViewById(R.id.dateEdit_back);
        name = (EditText) findViewById(R.id.name);

        add = (Button) findViewById(R.id.btn_add);
        cancel = (Button) findViewById(R.id.btn_cancel);
        myCalendar.setTimeInMillis(System.currentTimeMillis());
        currentCalendar.setTimeInMillis(System.currentTimeMillis());

        // set my Calendar date
        final DatePickerDialog.OnDateSetListener date = new DatePickerDialog.OnDateSetListener() {
            @Override
            public void onDateSet(DatePicker view, int year, int monthOfYear,
                                  int dayOfMonth) {
                years = year;
                months = monthOfYear;
                days = dayOfMonth;
                myCalendar.set(Calendar.YEAR, year);
                myCalendar.set(Calendar.MONTH, monthOfYear);
                myCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
                updateLabel();
            }
        };

        // when alarmDate editText is clicked
        alarmDate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                new DatePickerDialog(MainActivity2.this, date, myCalendar
                        .get(Calendar.YEAR), myCalendar.get(Calendar.MONTH),
                        myCalendar.get(Calendar.DAY_OF_MONTH)).show();
            }
        });

        // click listener on alarmClock EditText
        alarmClock.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                Calendar mcurrentTime = Calendar.getInstance();
                int hour = mcurrentTime.get(Calendar.HOUR_OF_DAY);
                int minute = mcurrentTime.get(Calendar.MINUTE);
                TimePickerDialog mTimePicker;
                mTimePicker = new TimePickerDialog(MainActivity2.this, new TimePickerDialog.OnTimeSetListener() {
                    @Override
                    public void onTimeSet(TimePicker timePicker, int selectedHour, int selectedMinute) {
                        alarmClock.setText(selectedHour + ":" + selectedMinute);
                        minutes = selectedMinute;
                        hours = selectedHour;
                        myCalendar.set(Calendar.HOUR_OF_DAY, selectedHour);
                        myCalendar.set(Calendar.MINUTE, selectedMinute - 1);
                        myCalendar.set(Calendar.SECOND, 59);
                    }
                }, hour, minute, true);//Yes 24 hour time
                mTimePicker.setTitle("Select Time");
                mTimePicker.show();
            }
        });

        final DatePickerDialog.OnDateSetListener date1 = new DatePickerDialog.OnDateSetListener() {
            @Override
            public void onDateSet(DatePicker view, int year, int monthOfYear,
                                  int dayOfMonth) {
                // TODO Auto-generated method stub
                years2 = year;
                months2 = monthOfYear;
                days2 = dayOfMonth;
                myCalendarRound.set(Calendar.YEAR, year);
                myCalendarRound.set(Calendar.MONTH, monthOfYear);
                myCalendarRound.set(Calendar.DAY_OF_MONTH, dayOfMonth);

                updateLabelRound();
            }
        };

        // when alarmDate editText is clicked
        alarmDateBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                new DatePickerDialog(MainActivity2.this, date1, currentCalendar
                        .get(Calendar.YEAR), currentCalendar.get(Calendar.MONTH),
                        currentCalendar.get(Calendar.DAY_OF_MONTH)).show();
            }
        });

        cancel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });

    }

    private void updateLabel() {
        String myFormat = "dd/MM/yyyy";
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.FRANCE);
        alarmDate.setText(sdf.format(myCalendar.getTime()));
    }

    private void updateLabelRound() {
        String myFormat = "dd/MM/yyyy";
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.FRANCE);
        alarmDateBack.setText(sdf.format(myCalendarRound.getTime()));
    }

}

