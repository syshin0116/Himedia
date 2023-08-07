import random
import random as ramdom
import turtle


def click(x, y):
    pensize = random.randint(1, 30)
    color_list = ['green', 'blue', 'yellow', 'red', 'purple', 'pink']
    color_choice = random.choice(color_list)
    print(color_choice)
    print(pensize)
    myTurtle.pensize(pensize)
    myTurtle.pencolor(color_choice)
    myTurtle.goto(x, y)
    print(x, y)
def goto(x, y):
    myTurtle.penup()
    myTurtle.goto(x, y)
    print(x, y)
    myTurtle.pendown()

x2 = random.randint(-400, 400)
y2 = random.randint(-400, 400)



while True:
    myTurtle = turtle.Turtle('turtle')
    turtle.onscreenclick(click, 1)
    # turtle.onscreenclick(goto, 1)
    turtle.done()

