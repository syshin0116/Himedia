from object.me import Day

if __name__ == '__main__':
    # 객체가 생성될 때 이니셜라이저 함수가 자동호출
    # 맴버변수가 복사된다
    day1 = Day('자바공부', 10, '강남')
    print(Day.count)
    day2 = Day('여행', 15, '강원도')
    print(Day.count)
    day3 = Day('운동', 11, '피트니스')
    print(Day.count)

    print(day1)
    print(day2)
    print(day3)


    print("전체 하는 일의 시간은: " + str(Day.total_time) + "시간")
    print("평균 하는 일의 시간은: " + str(Day.avg) + "시간")
    print("매일 무엇을 얼마나 어디에서 했는지 프린트: ")
    print("며칠 간 했는지?: ")