hobby3 = [
    {10: {'아침': 'game', '저녁': 'picture'}},
    {20: {'아침': 'game', '저녁': 'tour'}},
]
a100 = hobby3[1][20]['저녁']
print(a100)

hobby2 = {10: {'아침': 'game', '저녁': 'picture'}, 20: ['tour', 'run', 'coding']}
s100 = hobby2[10]
print(s100)
s1000 = s100['저녁']
print(s1000)
hobby = {10: ['game', 'picture'], 20: ['tour', 'run', 'coding']}
# 10대의 취미 목록을 프린트
print(hobby.get(10))

# 20대의 취미 목록을 프린트
print(hobby.get(20))
# 20대의 취미 목록을 카운트
print(len(hobby.get(20)))

food = {'아침': '토스트', '점심': '한정식', '저녁': '스프'}
print(food['아침']) # 값을 확인할 때: 딕셔너리이름[키]
food['아침'] = '커피' # 값을 수정할 때
print(food)
food['간식'] = '토스트'
print(food)

del food['간식']
print(food)

# dic를 for-each문으로 돌렸을때는 key만 가지고 온다.
for key in food:
    print(key+ '엔', food[key])

dict1 = {100 : '홍길동', 200:'kim', '300':'신'}
for key in dict1:
    print(key,'번',dict1[key])

key_list = dict1.keys()
print(key_list)
key_list2 = list(key_list)
print(key_list2)

value_list = dict1.values()
print(value_list)
value_list2 = list(value_list)
print(value_list2)

#print(dict1[100])
print(dict1.get(100))
print(100 in dict1)

#회원명단 중에서 500이 있나요?
if 500 in dict1:
    print('500회원이 존재합니다.')
else:
    print('존재하지 않습니다')