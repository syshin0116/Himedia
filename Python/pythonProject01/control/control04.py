no1 = int(input("숫자1: "))
no2 = int(input("숫자2: "))
print('no1+no2=', no1+no2)
print('no1-no2=', no1-no2)
print('no1*no2=', no1*no2)
print('no1/no2=', no1/no2)

name = input('입력1: ')
age = input('입력2: ')
print(name+'은 ' + age + '세입니다.')
if int(age) > 100:
    print("나이가 많으시군요!")
else:
    print("나이가 적으시군요!")

hobby = input("hobby= ")
time = input("time= ")
print(hobby+'를', time, '시간 했습니다.')
if hobby == '달리기' and time >= 10 :
    print("오늘'"+hobby+"'는 충분")
else :
    print("어떤 운동이든 시작학세요!!")

