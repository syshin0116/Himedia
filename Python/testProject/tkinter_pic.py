from tkinter import *
import random as r

root = Tk()
root.title('메뉴추천기')
root.config(padx=10, pady=10, bg='lightblue')

canvas = Canvas(root, height=680, width=680, bg='ivory')
canvas.pack()

btn1 = Button(root, text='한식', padx=20, font=('나눔바른펜', 20, 'bold'))
btn1.pack()
btn2 = Button(root, text='양식', padx=20, font=('나눔바른펜', 20, 'bold'))
btn2.pack()
btn3 = Button(root, text='중식', padx=20, font=('나눔바른펜', 20, 'bold'))
btn3.pack()
btn4 = Button(root, text='일식', padx=20, font=('나눔바른펜', 20, 'bold'))
btn4.pack()
btn5 = Button(root, text='분식', padx=20, font=('나눔바른펜', 20, 'bold'))
btn5.pack()

btn1.place(x=20, y=600)
btn2.place(x=150, y=600)
btn3.place(x=280, y=600)
btn4.place(x=410, y=600)
btn5.place(x=540, y=600)

root.mainloop()