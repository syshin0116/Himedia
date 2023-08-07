# 반복문
# 유한 루프
for i in range(0, 5, 2):
    print(i)
for i in [0, 1, 2, 3, 4, 5]:
    print(i, '내가 돌아.')

# 범위를 100부터 시작해서 100씩 점, 999까지 생성
for i in range(100,1000,100):
    print(i)

count = 0
while True:
    if count == 5:
        print('반복문 중지.')
        break
    print('내가 돌아@@@@@@@')
    count += 1
