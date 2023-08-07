# 주민번호 13자리를 입력을 받아서
# 나이와 성별을 판별해보세요.
import datetime

idnum = input("주민번호 13자리: ")
if idnum[0] == "0":
    age = 23 - int(idnum[:2])
else:
    age = 23 + 100 - int(idnum[:2])
if idnum[6] == "1" or idnum[6] == "3":
    gender = "남자"
elif idnum[6] == "2" or idnum[6] == "4":
    gender = "여자"
else:
    print("잘못 입력하셨습니다")
print("나이는 %d, 성별은 %s 입니다" % (age, gender))

# 현재 날짜

today = datetime.datetime.today()

print(today.year, today.month, today.day)
print(today.hour, today.minute, today.second)

sn = input('주민번호 13자리 입력>> ')
year = sn[:2] #0~1
gender = sn[6] #7
if gender == '1' or gender == '3':
    print('남자')
else :
    print('여자')

if gender in ('1', '3'):
    print('남자')
else :
    print('여자')

print('----------------')

year2 = int(year) + 1900 #int(), float(), str(), 그리고 list(), tuple(), set()
print(year2)

age = today.year - year2 + 1
print('age>> ', age)
