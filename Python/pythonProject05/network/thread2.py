import random
import threading
# 실(실처럼 작게 프로그램을 나누어서 처리)
# 동시프로그램


text = ['@', '#', '$', '\\']
def a1(x, y):
    for i in range(x, y+1):
        print('증가>>', i)
def a2(x, y):
    for i in range(x, y-1, -1):
        print('감소>>', i)
def a3():
    for i in range(100):
        print('특수>>', random.choice(text))


thread1 = threading.Thread(target=a1, args=(1, 100))
thread2 = threading.Thread(target=a2, args=(100, 1))
thread3 = threading.Thread(target=a3)

thread1.start() #cpu 스테쥴링에 thread1 대기줄에 세워줘
thread2.start() #cpu 스테쥴링에 thread1 대기줄에 세워줘
thread3.start() #cpu 스테쥴링에 thread1 대기줄에 세워줘