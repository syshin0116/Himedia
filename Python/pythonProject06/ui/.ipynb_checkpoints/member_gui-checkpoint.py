
from tkinter import *
from tkinter import messagebox
#버튼 개당 함수 1개
from PIL import ImageTk

from ui.member_dao import memberDAO

dao = memberDAO()

def save():
    id = id_entry.get()
    id_entry.delete(0, 'end')
    pw = pw_entry.get()
    pw_entry.delete(0, 'end')
    name = name_entry.get()
    name_entry.delete(0, 'end')
    tel = tel_entry.get()
    tel_entry.delete(0, 'end')
    print('입력한 id는 ', id, '입력한 pw는 ', pw, '입력한 name= ', name, '입력한 tel= ', tel)
    vo = (id, pw, name, tel)
    dao.create(vo)
def read():
    try:
        id = id_entry.get()
        data = dao.read(id)
        id, pw, name, tel = data
        # id를 주면서 검색
        pw_entry.insert(0, pw)
        name_entry.insert(0, name)
        tel_entry.insert(0, tel)
    except:
        error = Label(w,
                     text='error',
                     font=('comic sans', 20))
        error.pack()

w = Tk()
w.geometry("500x600")
# 라벨을 하나 만들어보자.
icon = PhotoImage(file='r7.png')
top = Label(w, image=icon)
top.pack()

# img = w.PhotoImage(file = "ask_img.jpg")
# img.pack()
id = Label(w,
           text = '아이디 입력',
           font = ('comic sans', 20)
           )
id.pack() #id라는 라벨을 w에 넣어줌
id_entry = Entry(w,
                 font = ('comic sans', 20),
                 bg = "light blue",
                 fg = "blue")
id_entry.pack()
pw = Label(w,
           text = '암호 입력',
           font = ('comic sans', 20))
pw.pack()
pw_entry = Entry(w,
                 font = ('comic sans', 20),
                 bg = "light blue",
                 fg = "blue")
pw_entry.pack()
name = Label(w,
           text = '이름 입력',
           font = ('comic sans', 20))
name.pack()
name_entry = Entry(w,
                 font = ('comic sans', 20),
                 bg = "light blue",
                 fg = "blue")
name_entry.pack()
tel = Label(w,
           text = '연락처 입력',
           font = ('comic sans', 20))
tel.pack()
tel_entry = Entry(w,
                 font = ('comic sans', 20),
                 bg = "light blue",
                 fg = "blue")
tel_entry.pack()
button = Button(w,
           text='DB에 저장',
           font=('comic sans', 20),
           bg='white',
           command=save
           ) #클릭버튼
button.pack()
read = Button(w,
           text='DB에서 읽어오기',
           font=('comic sans', 20),
           bg='white',
           command=read
           ) #클릭버튼
read.pack()
w.mainloop()