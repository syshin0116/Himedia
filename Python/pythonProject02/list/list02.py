#반복문은 2가지 경우에 사용
#1)횟수를 세기위해서
#2)반복하면서 어떤 처리를 하기 세기위해서

# for _ in range(5): #[0,1,2,3,4]:
#     print('환영합니다')
#
# sum = 0
# for n in range(1, 6):
#     sum += n
# print(sum)
#
# food = []
# food.append(input("음식1:"))
# food.append(input("음식2:"))
# food.append(input("음식3:"))
# print(food[1])
# print(food[0], food[1])
# food[0] = '라면'
# print(food)

month = []
for i in range(0, 2):
    month.append('겨울')
for i in range(2, 5):
    month.append('봄')
for i in range(5, 8):
    month.append('여름')
for i in range(8, 11):
    month.append('가을')
month.append('겨울')
print(month)

sum = 0
for n in range (10, 21):
    sum += n
print(sum)

answer = int(input("정답 숫자: "))
while True:
    guess = int(input("예상 숫자: "))
    if guess == answer:
        print("정답입니다!")
        break
    elif guess < answer:
        print("너무 작습니다")
    elif guess > answer:
        print("너무 큽니다")

no1 = int(input("시작값: "))
no2 = int(input("끝값: "))
sum = 0
for i in range(no1, no2):
    sum += i
sub = abs(no2 - no1)
avg = sum/sub
print("합:", sum, "사이 개수:", sub, "평균:%0.1f" %avg)