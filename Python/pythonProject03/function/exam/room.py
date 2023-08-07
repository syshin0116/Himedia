class TV:
    power = False
    sound = 0
    channel = 1

    def power_switch(self, power):
        if power == False:
            power = True
            print("TV가 켜졌습니다")
        elif power == True:
            power = False
            print("TV가 꺼졌습니다")

    def volume(self):
        sound = int(input("볼륨을 선택하세요: "))
        print("볼륨이 %d로 선택되었습니다" % sound)

    def surf(self, channel):
        channel = int(input("채널을 선택하세요: "))
        print("채널이 %d로 선택되었습니다" % channel)

    def __str__(self):
        return str(self.power) + ", " + str(self.sound) + ", " + str(self.channel)


if __name__ == '__main__':
    tv1 = TV()
    tv1.channel = 5
    print(tv1)
