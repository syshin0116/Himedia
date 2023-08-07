import random
import threading
import time
from tkinter import *


def finish(y1):
    rank = Label(window, text=place.pop())
    rank.place(x=200, y=y1)


class RacingCar:
    # 멤버변수
    name = ''

    # 초기화함수
    def __init__(self, name):
        # self: 클래스로 생성한 객체!
        # c1 = RacingCar('appleCar')
        # self == c1
        # c1.name = 'appleCar'
        self.name = name

    # 멤버함수

    def runCar(self, label, x1, y1):

        while True:
            jump = random.randint(1, 10)
            print(jump)
            x1 = x1 + jump
            label.place(x=x1 + jump, y=y1)
            if x1 >= 400:
                finish(y1)
                break
            time.sleep(0.05)


# def reset(window):
#     window.destroy()
#     window = Tk()

def run_start():
    global car_label1
    global car_label2
    global car_label3
    # 라벨 객체 만들어서 window에 끼워넣어야 함.
    print('call ok!!')
    ## 자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.
    c1 = RacingCar('appleCar')
    c2 = RacingCar('summerCar')
    c3 = RacingCar('springCar')

    t1 = threading.Thread(target=c1.runCar, args=(car_label1, 10, 200))
    t2 = threading.Thread(target=c2.runCar, args=(car_label2, 10, 250))
    t3 = threading.Thread(target=c3.runCar, args=(car_label3, 10, 300))

    t1.start()
    t2.start()
    t3.start()


def set_car():
    car1_img = PhotoImage(file='car1.gif')
    car2_img = PhotoImage(file='car2.gif')
    car3_img = PhotoImage(file='car3.gif')
    global car_label1
    global car_label2
    global car_label3
    car_label1 = Label(window, image=car1_img)
    car_label1.place(x=10, y=200)
    car_label2 = Label(window, image=car2_img)
    car_label2.place(x=10, y=250)
    car_label3 = Label(window, image=car3_img)
    car_label3.place(x=10, y=300)


if __name__ == '__main__':
    place = ["third", "second", "first!"]
    window = Tk()
    window.geometry("500x400")
    window.title('멀티 스레드 자동차 경주')

    s = Button(window, text='set',
               command=set_car)
    s.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)
    b = Button(window, text='멀티 스레드 시작',
               command=run_start)
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)

    car_label1 = Label()
    car_label2 = Label()
    car_label3 = Label()

    window.mainloop()
