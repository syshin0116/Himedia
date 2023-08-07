## member.txt에 member정보를 3명 넣으세요.
## file2.py에서 member.txt를 일겅오 ㄴ후
## 다음과 같이 출력되도록 해보세요.
## 이름   나이  연락처
## ---------------------
## hong 100 001
## park 150 019
## song 200 017
try:
    file = open('member.txt', 'w')
    for _ in range(3):
        name = input('당신의 이름은: ')
        age = input('당신의 나이는: ')
        tel = input('당신의 연락처는: ')
        data = name+ "\t" + age + "\t" + tel + "\n"
        file.write(data)
except FileNotFoundError:
    print('해당 파일을 찾을 수 없음')
except IOError:
    print('읽고 쓰는데 문제가 생겼음')
except:
    print('파일을 처리하는데 문제가 생겼음.')
finally:
    try:
        file.close()
    except:
        print('file을 closing하는데 문제가 생김')

