# spring(3, '제주도')
# => 3월에 제주도에 가요! 프린트
# summer('울릉도', 8) #default값 10000
# => 8월에 울룽도를 가는 비용은 10000원 입니다.
# => 조건처리 6이면 비용이 -2000 할인해서 8000원이 되도록
#            7이면 비용이 -1000할인해서 9000
#            나머지 월이면 +2000해서 12000

def spring(month, location):
    print("%d월에 %s에 가요!" %(month, location))
    # print(x, "월에", y+"에 가요!")


# defualt 로 설정하고 싶으면 파라미터 위치를 뒤에서부터
# 앞의 파라미터는 입력해주고, 입력해주지 않은 뒤의 파라미터를 default값으로 입력해주라고 처리되기 때문!
# ex) def summer(month, location, fee=10000)
def summer(month, location): #default값 10000
    fee = 10000
    if location == 6:
        fee -= 2000
    elif location == 7:
        fee -= 1000
    elif location == 8:
        pass
    else:
        fee += 2000
    print("%d월에 %s를 가는 비용은 %d원입니다"%(location, month, fee))
    # print(y, "월에", x+"를 가는 비용은", fee, "원 입니다.")

