import turtle as t

c = int(input('평균 하루 섭취 칼로리를 적어주세요  : '))

color_status = ['green', 'yellow', 'red']
alert_status = ['부족합니다', '적절합니다', '초과하였습니다']


def calorie(c):
    t.pensize(3)
    if 1900 <= c <= 2100:
        status = 0
    elif c < 1900:
        status = 1

    else:
        status = 2

    t.color(color_status[status])
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(-35, -50)
    t.pendown()
    t.write(alert_status[status])
    t.exitonclick()



calorie(c)
