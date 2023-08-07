import datetime as dt
import random
import threading
# 실(실처럼 작게 프로그램을 나누어서 처리)
# 동시프로그램
import time


def a1():
    now = dt.datetime.now()

    for i in range(100):
        time.sleep(1)
        print('시간>>', now)

def a2(x, y):
    for i in range(x, y+1):
        print('카운트>>', i)


def a3():
    text = ['아이스크림', '스시', '스파게티', '피자', '커피', '도넷', '소고기', '짜장면', '탕수육', '짬뽕']
    for i in range(10):
        time.sleep(1)
        for x in text:
            print('음식>>', x)


thread1 = threading.Thread(target=a1)
thread2 = threading.Thread(target=a2, args=(1, 500))
thread3 = threading.Thread(target=a3)

thread2.start()
thread3.start()
thread1.start()

