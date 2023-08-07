try:
    # test_file3 = open('text2.txt', 'w')
    test_file3 = open('text2.txt', 'a')
    test_file3.write('hello hi lunch\n')
    test_file3.write('hello2 hi2 lunch2\n')
    # result = test_file3.write('hello hi lunch')
    # print(result)
    # lines = test_file2.readlines()
    # for line in lines:
    #     print(line)
    # one = test_file2.readline()
    # print(one)
    # one2 = test_file2.readline()
    # print(one2)
    # one3 = test_file2.readline()
    # print(one3)
# except NameError:
#     print('해당 파일을 찾을 수 없음')
except FileNotFoundError:
    print('해당 파일을 찾을 수 없음')
except IOError:
    print('읽고 쓰는데 문제가 생겼음')
except:
    print('파일을 처리하는데 문제가 생겼음.')
finally:
    try:
        test_file3.close()
    except:
        print('file을 closing하는데 문제가 생김')

# 램에 만들어진 connection을 담당하는 stream 객체를
# 메모리에서 지우는 역할을 수행
# close함수를 호출하지 않으면 메모리에 계속 남아있어서
# 반드시 메모리에서 지워줘야 한다.
