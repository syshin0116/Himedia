from functools import partial
from tkinter import *
from tkinter import messagebox

import calc as calc

from 비전서비스카카오.cal import Calc


def getText(op):
    num = no_entry.get()
    print("gui에서 num: ", num)
    if Calc.ram == '':
        if op == '+':
            Calc.number = int(num)
            Calc.ram = '+'
        if op == '-':
            Calc.number = int(num)
            Calc.ram = '-'
        if op == '*':
            Calc.number = int(num)
            Calc.ram = '*'
        if op == '/':
            Calc.number = int(num)
            Calc.ram = '/'
    else:
        num = no_entry.get()
        if Calc.ram == '+':
            cal1.add(int(num))
            Calc.ram = op
        if Calc.ram == '-':
            cal1.subtract(int(num))
            Calc.ram = op
        if Calc.ram == '*':
            cal1.multiply(int(num))
            Calc.ram = op
        if Calc.ram == '/':
            cal1.divide(int(num))
            Calc.ram = op
    no_entry.delete(0, END)


def equal():
    num = no_entry.get()
    cal1.calc(int(num))
    print(Calc.number)

    messagebox.showinfo('결과값', Calc.number)


def reset():
    Calc.number = 0
    Calc.ram = ''
    no_entry.delete(0, END)


if __name__ == '__main__':
    cal1 = Calc()

    w = Tk()
    w.geometry("500x500")

    ask_no = Label(w,
                   text='숫자 입력',
                   font=('comic sans', 30)
                   )
    ask_no.pack()
    no_entry = Entry(w,
                     font=('comic sans', 30),
                     bg="light blue",
                     fg="blue")
    no_entry.pack()

    b1 = Button(w,
                text='+',
                font=('comic sans', 30),
                bg='white',
                command=partial(getText, '+')
                )
    b1.pack()
    b2 = Button(w,
                text='-',
                font=('comic sans', 30),
                bg='white',
                command=partial(getText, '-')
                )
    b2.pack()
    b3 = Button(w,
                text='x',
                font=('comic sans', 30),
                bg='white',
                command=partial(getText, '*')
                )
    b3.pack()
    b4 = Button(w,
                text='/',
                font=('comic sans', 30),
                bg='white',
                command=partial(getText, '/')
                )
    b4.pack()
    b_reset = Button(w,
                     text='CE',
                     font=('comic sans', 30),
                     bg='white',
                     command=reset
                     )
    b_reset.pack()
    b_calc = Button(w,
                    text='=',
                    font=('comic sans', 30),
                    bg='white',
                    command=partial(equal)
                    )
    b_calc.pack()
    w.mainloop()
