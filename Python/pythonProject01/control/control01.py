# 제어문
# 순차문: 입력--> 처리--> 출력
# 조건문: if, if~else, if~elif~..else
# 반복문: while, for
# 정리문제
# ----------
# 숫자입력>> 32
# 숫자입력>> 20
# 연산자 입력(+,-)>> +
# 두 수를 더한 결과는 52 입니다.
# 두 수를 뺀 결과는 12입니다.

no1 = input("숫자1 입력: ")
no2 = input("숫자2 입력: ")
function = input("연산자 입력(+,-): ")
if function == "+":
    result = int(no1) + int(no2)
    print("두 수를 더한 결과는", result, "입니다")
elif function == "-":
    result = int(no1) - int(no2)
    print("두 수를 뺀 결과는", result, "입니다")
else :
    print("잘못 입력하셨습니다")

