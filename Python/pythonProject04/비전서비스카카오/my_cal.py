from tkinter import *
from tkinter import messagebox



def add():
    numbers = []
    numbers.append(int(no1_entry.get()))
    numbers.append(int(no2_entry.get()))
    result = numbers[0]+numbers[1]
    messagebox.showinfo('결과값', result)

    print('입력한 no1은 ', numbers[0], '입력한 no2는 ', numbers[1])
def subtract():
    numbers = []
    numbers.append(int(no1_entry.get()))
    numbers.append(int(no2_entry.get()))
    result = numbers[0]-numbers[1]
    messagebox.showinfo('결과값', result)

    print('입력한 no1은 ', numbers[0], '입력한 no2는 ', numbers[1])
def multiply():
    numbers = []
    numbers.append(int(no1_entry.get()))
    numbers.append(int(no2_entry.get()))
    result = numbers[0]*numbers[1]
    messagebox.showinfo('결과값', result)

    print('입력한 no1은 ', numbers[0], '입력한 no2는 ', numbers[1])
def divide():
    numbers = []
    numbers.append(int(no1_entry.get()))
    numbers.append(int(no2_entry.get()))
    result = numbers[0]/numbers[1]
    messagebox.showinfo('결과값', result)

    print('입력한 no1은 ', numbers[0], '입력한 no2는 ', numbers[1])
def reset():
    no1_entry.delete(0, END)
    no2_entry.delete(0, END)
w = Tk()
w.geometry("500x500")

ask_no1 = Label(w,
           text = '숫자1 입력',
           font = ('comic sans', 30)
           )
ask_no1.pack()
no1_entry = Entry(w,
                 font = ('comic sans', 30),
                 bg = "light blue",
                 fg = "blue")
no1_entry.pack()

ask_no2 = Label(w,
           text = '숫자1 입력',
           font = ('comic sans', 30)
           )
ask_no2.pack()
no2_entry = Entry(w,
                 font = ('comic sans', 30),
                 bg = "light blue",
                 fg = "blue")
no2_entry.pack()

b1 = Button(w,
           text='+',
           font=('comic sans', 30),
           bg='white',
           command=add
            )
b1.pack()
b2 = Button(w,
           text='-',
           font=('comic sans', 30),
           bg='white',
           command=subtract
            )
b2.pack()
b3 = Button(w,
           text='x',
           font=('comic sans', 30),
           bg='white',
           command=multiply
            )
b3.pack()
b4 = Button(w,
           text='/',
           font=('comic sans', 30),
           bg='white',
           command=divide
            )
b4.pack()
b_reset = Button(w,
           text='CE',
           font=('comic sans', 30),
           bg='white',
           command=reset
            )
b_reset.pack()

w.mainloop()