import tkinter as tk
import pandas as pd
import os.path as path
from tkinter import BOTTOM, E, LEFT, RIGHT, messagebox
from numpy import pad
from openpyxl import load_workbook
from datetime import datetime

# 가격 및 선택 메뉴와 총 합계 변수들
price = {'아메리카노': 4500, '바닐라라떼': 5500, '자바 칩 프라푸치노': 6500, '자몽 허니 블랙 티': 6000,
         '리코타 치즈 샌드위치': 4900, '레드벨벳 크림치즈 케이크': 6400, '더블 에그 샐러드': 7500, '텀블러': 34000}
order_cnt = {'아메리카노': 0, '바닐라라떼': 0, '자바 칩 프라푸치노': 0, '자몽 허니 블랙 티': 0,
             '리코타 치즈 샌드위치': 0, '레드벨벳 크림치즈 케이크': 0, '더블 에그 샐러드': 0, '텀블러': 0}
select_menu = {}

order = []

sum = 0

# 고른 메뉴들의 수량과 총 주문금액을 나타내는 함수
def choice_menu(menu):
    global price, select_menu, sum

    if menu not in select_menu:
        select_menu[menu] = 1
    elif menu in select_menu:
        select_menu[menu] = select_menu.get(menu) + 1

    menus = price.get(menu)
    sum = sum + menus

    order.append(menu)
    order_cnt[menu] = order_cnt[menu] + 1

    layout_1['text'] = "총 주문금액:" + str(sum) + "원"
    text_menu()


# 메뉴들을 골랐을 때 고른 갯수를 키오스크에 표시하는 함수
def text_menu():
    global select_menu

    _choice = ""
    for menu in select_menu:
        _choice = _choice + menu + "  " + str(select_menu.get(menu)) + "\n"

    text_display.delete('1.0', tk.END)
    text_display.insert(tk.INSERT, _choice)


# 키오스크로 주문했던 내역들을 리셋해주는 함수
def reset():
    global name_entry, birth_entry, phone_entry, order, order_cnt, sum, select_menu

    text_display.delete('1.0', tk.END)

    layout_1['text'] = "총 주문금액:0원"

    order = []
    select_menu = {}
    order_cnt = {'아메리카노': 0, '바닐라라떼': 0, '자바 칩 프라푸치노': 0, '자몽 허니 블랙 티': 0,
                 '리코타 치즈 샌드위치': 0, '레드벨벳 크림치즈 케이크': 0, '더블 에그 샐러드': 0, '텀블러': 0}

    sum = 0

    name_entry.delete('0', tk.END)
    birth_entry.delete('0', tk.END)
    phone_entry.delete('0', tk.END)

    name_entry.focus()


# 엑셀로 주문내역 및 회원정보를 전송하고, 이는 영수증의 역할도 동시 수행한다
# 결제완료 시 reset함수가 실행되어 키오스크 주문내역 모두 삭제되는 함수
def receipt():
    global order, order_cnt, sum, name_entry, birth_entry, phone_entry
    columns_list = ['날짜', '이름', '생년월일', '전화번호', '아메리카노', '바닐라라떼', '자바 칩 프라푸치노', '자몽 허니 블랙 티', '리코타 치즈 샌드위치', '레드벨벳 크림치즈 케이크',
                    '더블 에그 샐러드', '텀블러', '총금액']
    date_now = datetime.today().strftime('%Y/%m/%d %H:%M:%S')
    birth = birth_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()
    print(type(phone))
    try:
        df = pd.read_csv('receipt_info.csv', header=0, index_col=[0])
    except:
        df = pd.DataFrame(columns=columns_list)

    menu_list = [date_now, name, birth, phone, order_cnt['아메리카노'], order_cnt['바닐라라떼'],
                 order_cnt['자바 칩 프라푸치노'], order_cnt['자몽 허니 블랙 티'],
                 order_cnt['리코타 치즈 샌드위치'], order_cnt['레드벨벳 크림치즈 케이크'], order_cnt['더블 에그 샐러드'], order_cnt['텀블러'], sum]

    df = pd.concat([df, pd.DataFrame([menu_list], columns=columns_list)], ignore_index=True).reset_index(drop=True)
    df.to_csv('receipt_info.csv')
    reset()


# 결제완료 버튼 함수
# 메뉴 미선택 시 결제진행이 되지 않는 오류창 발생
# 이름, 생년월일, 휴대폰번호 미입력 시 진행이 되지 않는 오류창 발생
def btn_complete():
    name = str(name_entry.get())
    birth = str(birth_entry.get())
    phone = str(phone_entry.get())

    if sum == 0:
        tk.messagebox.showerror('메뉴를 선택해주세요')
        return

    elif name == '':
        tk.messagebox.showerror('이름을 제대로 기입해주세요')
        name_entry.focus()
        return

    elif birth == '':
        tk.messagebox.showerror('생년월일을 제대로 기입해주세요')
        birth_entry.focus()
        return

    elif phone == '':
        tk.messagebox.showerror('휴대폰번호를 제대로 기입해주세요')
        phone_entry.focus()
        return

    msg_text = tk.messagebox.askquestion('확인', '주문을 완료하시겠습니까?')
    if msg_text == 'no':
        return
    elif msg_text == 'yes':

        receipt()


# 윈도우창 실행 및 제목과 키오스크화면의 크기를 고정해서 주문시 화면이 확대 및 축소 불가능하게 한다
# configure함수를 사용하여 키오스크의 배경색을 설정해 GUI를 꾸며준다
window = tk.Tk()
window.title("별다방 주문 키오스크")
window.geometry("1000x850+250+300")
window.resizable(False, False)
window.configure(background='mediumseagreen')

# 메뉴 및 결제완료 버튼들의 프레임을 잡아준다
linear_layout_1 = tk.Frame(window)
linear_layout_1.pack()

# 회원정보 입력하는 칸들의 프레임을 잡아준다
linear_layout_2 = tk.Frame(window)
linear_layout_2.pack()

# 각종 버튼과 크기 및 위치 설정
btn_coffee = tk.Button(linear_layout_1, text="         아메리카노         \n4,500원", command=lambda: choice_menu('아메리카노'),
                       padx=20, pady=5, font='times', fg="coral")
btn_coffee.grid(row=0, column=0, padx=30, pady=30)

btn_latte = tk.Button(linear_layout_1, text="              바닐라라떼              \n5,500원",
                      command=lambda: choice_menu('바닐라라떼'),
                      padx=20, pady=5, font='times', fg="silver")
btn_latte.grid(row=0, column=1, padx=30, pady=15)

btn_frappuccino = tk.Button(linear_layout_1, text="자바 칩 프라푸치노\n6,500원", command=lambda: choice_menu('자바 칩 프라푸치노'),
                            padx=20, pady=5, font='times', fg="chocolate")
btn_frappuccino.grid(row=0, column=2, padx=30, pady=15)

btn_tea = tk.Button(linear_layout_1, text="자몽 허니 블랙 티\n6,000원", command=lambda: choice_menu('자몽 허니 블랙 티'),
                    padx=20, pady=5, font='times', fg="orangered")
btn_tea.grid(row=0, column=3, padx=30, pady=15)

btn_sandwich = tk.Button(linear_layout_1, text="리코타 치즈 샌드위치\n4,900원", command=lambda: choice_menu('리코타 치즈 샌드위치'),
                         padx=20, pady=5, font='times', fg="gold")
btn_sandwich.grid(row=1, column=0, padx=30, pady=15)

btn_cake = tk.Button(linear_layout_1, text="레드벨벳 크림치즈 케이크\n6,400원", command=lambda: choice_menu('레드벨벳 크림치즈 케이크'),
                     padx=20, pady=5, font='times', fg="darkred")
btn_cake.grid(row=1, column=1, padx=30, pady=15)

btn_salad = tk.Button(linear_layout_1, text="   더블 에그 샐러드   \n7,500원", command=lambda: choice_menu('더블 에그 샐러드'),
                      padx=20, pady=5, font='times', fg="mediumaquamarine")
btn_salad.grid(row=1, column=2, padx=30, pady=15)

btn_tumblr = tk.Button(linear_layout_1, text="          텀블러         \n34,000원", command=lambda: choice_menu('텀블러'),
                       padx=20, pady=5, font='times', fg="teal")
btn_tumblr.grid(row=1, column=3, padx=30, pady=15)

btn_finish = tk.Button(linear_layout_1, text="결제완료", command=btn_complete, padx=20, pady=5, font='times', fg="skyblue")
btn_finish.grid(row=2, column=3, padx=15, pady=50)

# 메뉴들을 선택할 때, 실시간으로 가격 표시하는 레이아웃
layout_1 = tk.Label(window, text="총 주문금액 : 0원", width=20, height=15, fg="darkcyan")
layout_1.pack(side=RIGHT)
layout_1.configure(background='beige')

# 이름을 나타내는 레이아웃 및 입력하기 위한 식
layout_2 = tk.Label(linear_layout_2, text="이름", width=66, height=3, fg="cornflowerblue")
layout_2.grid(row=0, column=0)
name_entry = tk.Entry(linear_layout_2)
name_entry.place(x=500, y=13)

# 생년월일을 나타내는 레이아웃 및 입력하기 위한 식
layout_3 = tk.Label(linear_layout_2, text="생년월일", width=66, height=3, fg="lightskyblue")
layout_3.grid(row=1, column=0)
birth_entry = tk.Entry(linear_layout_2)
birth_entry.place(x=500, y=67)

# 휴대폰번호를 나타내는 레이아웃 및 입력하기 위한 식
layout_4 = tk.Label(linear_layout_2, text="휴대폰번호", width=100, height=3, fg="deepskyblue")
layout_4.grid(row=2, column=0)
phone_entry = tk.Entry(linear_layout_2)
phone_entry.place(x=500, y=120)

# 메뉴 및 갯수를 나타내기 위한 값 및 여백
text_display = tk.Text(window)
text_display.pack(side=BOTTOM, padx=250, pady=60)
text_display.configure(background='powderblue')

# 윈도우 내부에서 수행되는 이벤트들이 발생하게 해주는 함수
window.mainloop()

if __name__ == '__main__':
    print(0)