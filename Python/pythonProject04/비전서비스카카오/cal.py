from tkinter import *
from tkinter import messagebox

class Calc:
    number = 0
    ram = ''
    result = 0
    post_num = 0

    def add(self, number):
        Calc.number += number
        print('입력한 no은 ', number, "result = ", Calc.number)

    def subtract(self, number):
        Calc.number -= number
        print('입력한 no은 ', number, "result = ", Calc.number)

    def multiply(self, number):
        Calc.number *= number
        print('입력한 no은 ', number, "result = ", Calc.number)

    def divide(self, number):
        Calc.number /= number
        print('입력한 no은 ', number, "result = ", Calc.number)

    def calc(self, number):
        print("calc에서 num: ", number)
        print("calc에서 계산전 Calc.number: ", Calc.number)
        print("ram", Calc.ram)
        if Calc.ram == "+":
            print(type(Calc.number))
            Calc.number += number

        if Calc.ram == "-":
            Calc.number -= number

        if Calc.ram == "*":
            Calc.number *= number

        if Calc.ram == "/":
            Calc.number /= number
