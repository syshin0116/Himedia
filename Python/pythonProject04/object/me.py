class Day:
    doing = '' # 인스턴스 변수
    time = 0 #인스턴스 변수
    location = '' #인스턴스 변수
    count = 0 #누적용, #클래스 변수
    avg = 0 #클래스 변수
    total_time = 0 #클래스 변수
    def __init__(self, doing, time, loocation):
        self.doing = doing
        self.time = time
        self.location = loocation
        # 이니셜라이저가 호출 될 때 마다
        # 몇개의 객체가 생성되었는지 누적!
        Day.count += 1
        Day.total_time += time
        Day.avg = Day.total_time / Day.count

    def study(self):
        print(self.doing + '을 열심히하다.')

    def __str__(self):
        return self.doing + ' ' + \
                str(self.time) + ' ' + \
                self.doing