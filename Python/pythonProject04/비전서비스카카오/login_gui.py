from tkinter import *
from tkinter import messagebox
#버튼 개당 함수 1개



def login():
    #입력값 가지고 오고, 일치하는지 확인
    id2 = id_entry.get()
    pw2 = pw_entry.get()
    print('입력한 id는 ', id2, '입력한 pw는 ', pw2)
    # 원래의 id/pw와 입력한 id/pw가 동일한지 판별하여 프린트
    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인 성공', '로그인 성공!')
        print('로그인 성공')
    else:
        messagebox.showinfo('로그인 실패', '로그인 실패!')
        print('로그인 실패')


w = Tk()
w.geometry("500x250")
#라벨을 하나 만들어보자.
id = Label(w,
           text = '아이디 입력',
           font = ('comic sans', 30)
           )
id.pack() #id라는 라벨을 w에 넣어줌
id_entry = Entry(w,
                 font = ('comic sans', 30),
                 bg = "light blue",
                 fg = "blue")
id_entry.pack()
pw = Label(w,
           text = '암호 입력',
           font = ('comic sans', 30))
pw.pack()
pw_entry = Entry(w,
                 font = ('comic sans', 30),
                 bg = "light blue",
                 fg = "blue")
pw_entry.pack()
b = Button(w,
           text='로그인 처리',
           font=('comic sans', 30),
           bg='white',
           command=login
           ) #클릭버튼
b.pack()
w.mainloop()