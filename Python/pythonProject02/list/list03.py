ticket = []
for i in range(10):
    ticket.append('0')
print('----------------------------------------------------')
print('  ', end='')
for x in range(1,11):
    print(x, end='    ')
print()
print(ticket)
print('----------------------------------------------------')
menu = 0
taken = 0
money = 0
while True:
    print("영화 예매 싸이트입니다")
    print("1. 예약 2. 예약 취소 3. 예약 변경 q: 종료")
    menu = input("메뉴 입력: ")
    if menu == "1":
        if ticket == ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]:
            print("모든 좌석이 찼습니다")
        else:
            print('----------------------------------------------------')
            print('  ', end='')
            for x in range(1, 11):
                print(x, end='    ')
            print()
            print(ticket)
            print('----------------------------------------------------')
            number = int(input("예약 인원수: "))
            for i in range (number):
                print("현재 자리:")
                print(ticket)
                seat = int(input("몇번 자리를 예약하시겠습니까? (현재 %d명째 예약): " %(i+1)))
                if ticket[seat] == '1':
                    print("이미 예약된 자리입니다. 다시 입력해주세요")
                    i -= 1
                else:
                    ticket[seat] = '1'
                    print("예약되었습니다")
                    taken += 1
                    print("현재 예약된 자리수: %d" % taken)
                    money = 10000 * number
                    print("금액: %d" % money)

    elif menu == "2":
        if ticket==["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]:
            print("예약된 좌석이 없습니다")
        else:
            print(ticket)
            number = int(input("취소할 인원수: "))
            for i in range(number):
                print("현재 자리:")
                print('----------------------------------------------------')
                print('  ', end='')
                for x in range(1, 11):
                    print(x, end='    ')
                print()
                print(ticket)
                print('----------------------------------------------------')
                seat = int(input("몇번 자리를 예약 취소 하시겠습니까? (현재 %d명째 예약 취소): " % (i + 1)))
                ticket[seat] = '0'
                print("예약 취소되었습니다")
                taken -= 1
                print("현재 예약된 자리수: %d" % taken)
                print(ticket)
    elif menu == "3":
        if ticket==["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]:
            print("예약된 좌석이 없습니다")
        else:
            print('----------------------------------------------------')
            print('  ', end='')
            for x in range(1, 11):
                print(x, end='    ')
            print()
            print(ticket)
            print('----------------------------------------------------')
            number = int(input("예약 변경할 인원수: "))
            for i in range(number):
                print("현재 자리:")
                print('----------------------------------------------------')
                print('  ', end='')
                for x in range(1, 11):
                    print(x, end='    ')
                print()
                print(ticket)
                print('----------------------------------------------------')
                seat_b = int(input("기존 예약 자리가 몇번이였습니까?(현재 %s명째 예약 변경): " %(i + 1)))
                ticket[seat_b] = '0'
                print("기존 자리가 예약 취소되었습니다")
                print(ticket)
                seat = int(input("몇번 자리를 예약하시겠습니까? (현재 %s명 예약 변경): " % (i + 1)))
                if ticket[seat] == '1':
                    print("이미 예약된 자리입니다")
                    i -= 1
                else:
                    ticket[seat] = '1'
                    print("새 자리가 예약되었습니다")
                    print('----------------------------------------------------')
                    print('  ', end='')
                    for x in range(1, 11):
                        print(x, end='    ')
                    print()
                    print(ticket)
                    print('----------------------------------------------------')
    elif menu == "q":
        break
    else:
        print("잘못입력했습니다")