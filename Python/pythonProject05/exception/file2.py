try:
    file = open('member.txt', 'r')
    lines = file.readlines()
    print("이름\t\t나이\t\t연락처")
    print("--------------------------")
    for line in lines:
        name, age, tel = line.split('\t')
        data = name + "\t" + age + "\t\t" + tel
        print(data, end="")
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
