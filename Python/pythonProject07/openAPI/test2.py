# import os
# print(os.path.abspath('test02.jpg'))
#
# # C:\Users\hi\Desktop\승엽\HimediaPython\pythonProject07\openAPI\test02.jpg

# 1.변의 길이를 입력받고, 빈 직삼각형 출력
# 2.가로, 세로 길이를 입력받고, 빈 직사각형 출력
# 3.높이를 입력받고, 빈 마름모 출력
num = int(input("변의 길이:"))
for i in range((num+1)//2):
    if i == 0 :
        print(" "*(num//2)+"*")
    else:
        print(' '*((num//2)-i)+"*"+" "*((i*2)-1)+"*")
