import random

no_of_students = int(input('학생 수:'))

# 보기 list 생성
a_list = []
if no_of_students//2==0:
    for i in range((no_of_students+1) * no_of_students / 2):
        a_list.append(i)
else:
    for i in range((no_of_students+1) * int(no_of_students / 2) + (int(no_of_students / 2) + 1)):
        a_list.append(i)

print(len(a_list))

# 보기 list에서 중복값 제거
a_list = list(set(a_list))

# 결과값 저장할 dictionary
answer_dict = {}

# 135명당
for i in range(1, no_of_students+1):
    # 학생마다 빈 임시 리스트 생성
    temp_list = []
    # 임시 리스트에 학생수만큼 보기 리스트에서 pop해서 append
    for j in range(i):
        temp_list.append(a_list.pop(random.randint(1, len(a_list)-1)))
    # 임시리스트를 결과dict에 학생번호 index로 저장
    answer_dict[i] = temp_list

print(answer_dict)
