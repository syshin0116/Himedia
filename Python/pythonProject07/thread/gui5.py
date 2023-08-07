# 클릭을 했을 대, 두 가지 그림을 그리는 함수를 만들어보세요.
# 아무거나 둘 선택
# color, size 변하게
import random
import turtle



def click(x, y):
    pensize = random.randint(1, 30)
    color_choice = random.choice(color_list)

    print(color_choice)
    print(pensize)
    myTurtle.pensize(pensize)
    myTurtle.pencolor(color_choice)
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()

    print(x, y)
def shape():
    print("shape")
    for _ in range(20):
        myTurtle.right(126)
        myTurtle.forward(100)
def star():
    print("star")
    for _ in range(5):
        myTurtle.right(144)
        myTurtle.forward(100)

def moveUp():
    myTurtle.setheading(90)
    myTurtle.forward(10)
def moveDown():
    myTurtle.setheading(270)
    myTurtle.forward(10)
def moveRight():
    myTurtle.setheading(0)
    myTurtle.forward(10)
def moveLeft():
    myTurtle.setheading(180)
    myTurtle.forward(10)
color_list = ['green', 'blue', 'yellow', 'red', 'purple', 'pink']
myTurtle = turtle.Turtle('turtle')
myTurtle.speed(0)
while True:

    turtle.onkeypress(star, 'space')
    turtle.onkeypress(shape, 't')
    turtle.onkeypress(moveUp, 'Up')
    turtle.onkeypress(moveRight, 'Right')
    turtle.onkeypress(moveLeft, 'Left')
    turtle.onkeypress(moveDown, 'Down')
    turtle.listen()
    turtle.onscreenclick(click, 1)
    turtle.done()
