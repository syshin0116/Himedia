import math

common_div = []
for i in range(12+1):
num = math.gcd(8, 12)+1
print("num>>", num)
answer = (8*12)-((12*2)-(num+1)*2)
print(answer)