import turtle
screen = turtle.Screen()
screen.bgpic('background.png')
screen.addshape('icon1.gif')
screen.addshape('icon2.gif')
screen.addshape('icon3.gif')

icon1 = turtle.Turtle('icon1.gif')
icon2 = turtle.Turtle('icon2.gif')
icon3 = turtle.Turtle('icon3.gif')

icon1.shapesize(1)
icon2.shapesize(3,4)
icon3.shapesize(5,6)

screen.mainloop()