from inherit.mobile import SamsungPhone, Phone, ApplePhone

p1 = Phone()
s1 = SamsungPhone('sam')
a1 = ApplePhone(10)

p1.text()
p1.call()

s1.game()
s1.internet(3)

a1.picture()
a1.youtube(2, '스포츠')