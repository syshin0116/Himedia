class Shop:
    location = "서울"
    owner = "주인장"

    def open(self):
        print('가게가 열렸습니다')

    def close(self):
        print("가게가 닫았습니다")

    def total_price(self, num, price):
        total = num * price
        print("총 결제금액은 %d원 입니다" %total)

    def total_count(self, visit, avg = 100):
        today = visit - avg
        print("오늘은 평균보다 %d명 많이 들어왔어요"%today)

if __name__ == '__main__':
    shop1 = Shop()
    print(shop1.owner)
