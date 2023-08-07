class Bike:
    # 멤버변수 3개
    # 멤버함수 3개
    # 객체 1개 b1만 생성해서, 멤버변수값 넣고, 프린트
    # 멤버변수 2개 이상 호출. (return X, return O)
    color = ''
    price = 0
    company = ''
    def __init__(self, color, price, company):
        self.color = color
        self.price = price
        self.company = company

    def change_color(self, color_change):

        print(self.color + "색의 자전거가 " + color_change + "색의 자전거로 색이 바뀌었습니다.")
        self.color = color_change

    def set_price(self, price_change):
        print(self + "자전거의 가격이 " + self.price + "에서 " + price_change + "로 바뀌었습니다")

    def set_company(self, company_change):
        print(self + "자전거의 제작사가" + self.company + "로 변경되었습니다")

    def __str__(self):
        return self.color + ', ' + str(self.price) + ', ' + self.company


class Car:
    # member변수
    color = ''
    shape = ''
    #이니셜라이저(멤버변수 초기화할 목저으로 만들어두는 함수)
    #객체생성시 자동호출됨
    #객체가 2개가 만들어지면, 2번 호출!

    def __init__(self, color, shape):
        self.color = color
        self.shape = shape


    # member함수
    def speed_up(self):
        print(self.color + '색인 자동차의 속도를 up!')

    def speed_down(self):
        print('자동차의 속도를 down!')

    def __str__(self):
        return self.color + ', ' + self.shape
