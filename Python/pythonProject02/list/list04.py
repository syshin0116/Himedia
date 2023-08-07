# Battleship game 신승엽

import random

bship1 = []
bship2 = []
bship1_shot = []
hitcount1 = 0
hitcount2 = 0
#플레이어, 컴퓨터, 쏜 자리 빈칸(0)으로 만듬
for i in range(20):
    bship1.append(0)
    bship2.append(0)
    bship1_shot.append(0)

# 플레이어진영, 쏜자리 그림
print()
print(' ', end='')
for x in range(1,10):
    print(x, end='  ')
for x in range(10,21):
    print(x, end=' ')
print()
print(bship1)
print("플레이어 진영")
print('---------------------------------------------------------------')
print("플레이거가 쏜 자리")
print(bship1_shot)
print(' ', end='')
for x in range(1,10):
    print(x, end='  ')
for x in range(10,21):
    print(x, end=' ')
print()
print()


#플레이어 배 위치 선정
# p1_list = [input() for _ in range(3)]
p1 = input("플레이어1) 선정할 배 위치 좌표 3개를 입력해주세요 ex)1,2,3 \n")

p1_list = p1.split(',')
p1_list = [int(n) for n in p1_list]
for i in p1_list:
    bship1[(i-1)] = 1
#컴퓨터 배 위치 랜덤으로 선정

p2 = random.randint(1,20)
bship2[(p2-1)] = 1
bship2[(p2)] = 1
bship2[(p2+1)] = 1


# 플레이어진영, 쏜자리 그림
print(' ', end='')
for x in range(1,10):
    print(x, end='  ')
for x in range(10,21):
    print(x, end=' ')
print()
print(bship1)
print("플레이어 진영")
print('---------------------------------------------------------------')
print("플레이거가 쏜 자리")
print(bship1_shot)
print(' ', end='')
for x in range(1,10):
    print(x, end='  ')
for x in range(10,21):
    print(x, end=' ')
print()
print()

##게임 시작
print("선공입니다")
#while문으로 한쪽이 이길때까지 반복
while True:
    # 플레이어진영, 쏜자리 그림
    print(' ', end='')
    for x in range(1, 10):
        print(x, end='  ')
    for x in range(10, 21):
        print(x, end=' ')
    print()
    print(bship1)
    print("플레이어 진영")
    print('---------------------------------------------------------------')
    print("플레이거가 쏜 자리")
    print(bship1_shot)
    print(' ', end='')
    for x in range(1, 10):
        print(x, end='  ')
    for x in range(10, 21):
        print(x, end=' ')
    print()
    print()

    # 플레이어가 이긴 경우
    if hitcount1 == 3:
        print("플레이어 승리!!!!!")
        break
    # 컴퓨터가 이긴 경우
    elif hitcount2 == 3:
        print("컴퓨터 승리!!!!!!")
        break

    #아직 승부가 나지 않은 경우
    else:
        print("플레이어: %d 컴퓨터: %d" %(hitcount1, hitcount2))
        print("공격 차례")
        p1_shot = input("쏠 좌표 3개를 지정해주세요 ex)1,2,3 \n")
        p1_list = p1_shot.split(',')
        p1_list = [int(n) for n in p1_list]
        for i in p1_list:

            if bship2[(i-1)] == 1:
                bship1_shot[(i - 1)] = 3
                print("hit!!!")
                hitcount1 += 1
            else:
                print("miss!!!")
                bship1_shot[(i - 1)] = 1
        print("컴퓨터가 공격합니다")
        for i in range(3):
            p2_shot = random.randint(0, 20)
            if bship1[i] == 1:
                print("컴퓨터: hit!!")
                bship1[i] = 3
                hitcount2 += 1
            else:
                print("컴퓨터: miss!!!!!")
