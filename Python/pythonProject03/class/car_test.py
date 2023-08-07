class Car:
    color = None
    speed = 0

    #self == this(java)
    #해당 class, Car
    def start(self):
        print('차가 출발하다.')


    def stop(self):
        print('차가 멈추다.')


    def __str__(self):
        return str(self.color) + ", " + str(self.speed)


if __name__ == '__main__':
    # Car car1 = new Car()
    car1 = Car()
    car2 = Car()
    car1.color = 'red'
    car1.speed = 300

    car2.color = 'black'
    car2.speed = 400
    print(car1)
    print(car2)
