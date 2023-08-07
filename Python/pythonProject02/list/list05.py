
import random
u_list = [0] * 10
m_list = [0] * 10
u_attack = [0] * 10
m_attack = [0] * 10

#배위치
for _ in range(3):
    my = int(input("내 배 위치입력:"))
    m_list[my] = 1


for _ in range(3):
    you1 = random.randint(0, 9);
    u_list[you1] = 1

#폭탄
for _ in range(3):
    my = int(input("내 폭탄 위치입력:"))
    m_attack[my] = 1

for _ in range(3):
    you1 = random.randint(0, 9);
    u_attack[you1] = 1




print("----------------------------")
print("내위치:", m_list)
print("내폭탄위치:",  m_attack)
print("----------------------------")

count=0;
count1=0;

while True:
    if count1==3 or count==3:
        if count1==3:
            print("졌음")
        if count == 3:
            print("이겼음")
        break

    for _ in range(3):
        my = int(input("내 폭탄 위치입력:"))
        m_attack[my] = 1

    for _ in range(3):
        you1 = random.randint(0, 9);
        u_attack[you1] = 1
    for i in range(0, 10, 1):
        if u_list[i] == m_attack[i]:
            if u_list[i] == 1 and m_attack[i] == 1:
                count = count + 1
                print()
                print(count, ":폭격성공", ", 성공위치: ", i)
                u_list[i] = "_"
        if m_list[i] == u_attack[i]:
            if m_list[i] == 1 and u_attack[i] == 1:
                count1 = count1 + 1
                print()
                print(count, ":폭격성공", ", 성공위치: ", i)
                u_list[i] = "_"


print(u_list)
print(m_list)



