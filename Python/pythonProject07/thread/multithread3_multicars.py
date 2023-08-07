import random
import threading
import time
from tkinter import *


def finish(y1):
    try:
        rank = Label(w, text=place.pop())
        rank.place(x=w.winfo_width()/2, y=y1)
    except:
        pass

class Fullscreen_Window(Tk):


    def __init__(self):
        self.tk = Tk()
        self.tk.geometry("500x1000")
        self.tk.title('멀티 스레드 자동차 경주')
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("f", self.toggle_fullscreen)
        self.tk.bind("e", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

class RacingCar:
    # 멤버변수
    # 멤버함수

    def runCar(self, label, x1, y1):

        while True:
            jump = random.randint(1, 10)
            print(jump)
            x1 = x1 + jump
            label.place(x=x1 + jump, y=y1)
            if x1 >= w.winfo_width()-100:
                finish(y1)
                break
            time.sleep(0.05)


# def reset(window):
#     window.destroy()
#     window = Tk()

def run_start():
    # 라벨 객체 만들어서 window에 끼워넣어야 함.
    print('call ok!!')
    ## 자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.
    global num_car
    global car_list
    global car_imglist
    c_list = []
    t_list = []
    print(num_car)
    for i in range(num_car):
        c_list.append('c'+str(i+1))
        t_list.append('t'+str(i+1))
        # globals()['c{}'.format(i)] = RacingCar()
    for i in range(num_car):
        c_list[i] = RacingCar()
        t_list[i] = threading.Thread(target=c_list[i].runCar, args=(car_list[i], 10, 200+i*50))
        t_list[i].start()
    # c1 = RacingCar('appleCar')
    # c2 = RacingCar('summerCar')
    # c3 = RacingCar('springCar')
    #
    # t1 = threading.Thread(target=c1.runCar, args=(car_label1, 10, 200))
    # t2 = threading.Thread(target=c2.runCar, args=(car_label2, 10, 250))
    # t3 = threading.Thread(target=c3.runCar, args=(car_label3, 10, 300))
    #
    # t1.start()
    # t2.start()
    # t3.start()


def set_car():
    global car_imglist # 자동차당 PhotoImage(file="car1~3.gif")
    global car_list # car_label1~ list
    global num_car # 입력받은 자동차수
    num_car = int(carnum_entry.get()) # 자동차수 입력받은 값 전달받고 입력칸 초기화
    carnum_entry.delete(0, 'end')
    print("입력값",num_car)

    for i in range(num_car): # 자동차수대로 리스트 만들기
        # car_img.append(car_imglist[car%3])
        # globals()['car{}_img'.format(car+1)] = PhotoImage(file=globals()['car{}.gif'.format((car+1)%3)])
        # globals()['car_label{}'.format(car+1)] = Label(w, image=globals()['car{0}_img'.format(car+1)])
        # globals()['car_label{}'.format(car+1)].place(x=10, y=200+(car+1*50))
        car_imgname = "car" + str(i + 1) + "_img"
        # "car"+str((car%3)+1)+".gif"
        car_imglist.append(car_imgname)
        car_list.append("car_label"+str(i+1))
    print("car_imglist =", car_imglist)
    print("car_list =", car_list)
    for i in range(num_car): #car1_img = PhotoImage(file='car1.gif'), car1_img = PhotoImage(file='car1.gif')
        car_imglist = PhotoImage(file="car"+str((i%3)+1)+".gif")
        car_list[i] = Label(w, image=car_imglist)
        car_list[i].image = car_imglist
        car_list[i].place(x=10, y=200+50*i)

    # car1_img = PhotoImage(file='car1.gif')
    # car2_img = PhotoImage(file='car2.gif')
    # car3_img = PhotoImage(file='car3.gif')
    #
    # car_label1 = Label(w, image=car1_img)
    # car_label1.place(x=10, y=200)
    # car_label2 = Label(w, image=car2_img)
    # car_label2.place(x=10, y=250)
    # car_label3 = Label(w, image=car3_img)
    # car_label3.place(x=10, y=300)


if __name__ == '__main__':
    place = ["THIRD", "SECOND", "FIRST!"]
    num_car = 0
    car_list = []
    car_imglist = []
    w = Fullscreen_Window()
    carnum = Label(w,
               text='차 개수 입력',
               font=('comic sans', 20)
               )
    carnum.pack()  # id라는 라벨을 w에 넣어줌
    carnum_entry = Entry(w,
                     font=('comic sans', 20),
                     bg="light blue",
                     fg="blue")
    carnum_entry.pack()

    s = Button(w, text='set',
               command=set_car)
    s.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)
    b = Button(w, text='멀티 스레드 시작',
               command=run_start)
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)
    w.tk.mainloop()