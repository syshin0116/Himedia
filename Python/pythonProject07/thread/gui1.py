import turtle

t = turtle.Pen()

while True:
    direction = input("1)네모, 오른쪽:right q: quit>> ")
    angle = int(input("각도>> "))
    if direction == 'left':
        t.left(angle)
        t.forward(300)
    elif direction == 'right':
        t.right(angle)
        t.forward(300)
    elif direction == 'q':
        break

