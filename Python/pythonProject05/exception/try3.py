food = ['coffee', 'water']

try:
    food[2] = 'juice'
    result = 3 / 0
    print(result)
# 인덱스에러이면, 첫번째 인덱스에 juice라고 넣어 예외처리
# zero로 나누는 에러이면, '특별히 예외처리할 내용이 없음' 이라고 프린트
# 마지막에 반드시 "필요한 예외처리를 하였음"이라고 프린트
except IndexError as index:
    print(index)
    food[0] = 'juice'

except ZeroDivisionError:
    print('특별히 예외처리할 내용이 없음')
print(food)
print("필요한 예외처리를 하였음")