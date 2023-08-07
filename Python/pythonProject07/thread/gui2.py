import turtle

t = turtle.Pen()
def click(x, y):
    print(x, y)

while True:
    while True:
        direction = input("1)네모, 2)별 3)별2 q) quit>> ")
        if direction == '1':
            for _ in range(4):
                t.forward(300)
                t.left(90)
        elif direction == '2':
            for _ in range(5):
                t.right(144)
                t.forward(100)
                # t.left(150)
                # t.forward(100)
        elif direction == '3':
            for _ in range(20):
                t.right(126)
                t.forward(100)
        elif direction == 'q':
            break
    t.onclick(click)

