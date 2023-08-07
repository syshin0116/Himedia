#북마크 테이블에 대한 crud 기능 처리를 하고 싶음.

# from db import dao
# from 패키지 import 모듈명
# --> 모듈, 함수(), 모듈명, 클래스명()
import sys
from tkinter import messagebox

from db.member_dao import *
# from 패키지명.모듈명 import 함수명, 클래스명, *
# --> 함수() 로 사용 가능


if __name__ == '__main__':
    dao = memberDAO()
    while(True):
        choice = int(input('CUD중 선택>> 1)C, 2)U, 3)D 4)R(one) 5)R(all) >> '))
        if choice == 1:
            id = input('id입력>> ')
            pw = input('pw입력>> ')
            name = input('name입력>> ')
            tel = input('tel입력>> ')
            vo = (id, pw, name, tel)
            # create(id, name, url, img)
            dao.create(vo)
        elif choice == 2:
            id = input('변경할 id입력>> ')
            pw = input('pw입력>> ')
            name = input('name입력>> ')
            tel = input('tel입력>> ')
            vo = (id, pw, name, tel)
            dao.update(vo)
            # id가 1이면, name은 naver2로 변경
        elif choice == 3:
            id = input('삭제할 id입력>> ')
            vo = id
            dao.delete(vo)
            # id가 1이면 삭제
        elif choice == 4:
            id = input('검색할 id입력>> ')
            row = dao.read(id)
            # id를 주면서 검색
            messagebox.showinfo('결과', '검색결과는: '+ row[0] + '\t' + row[1] + '\t' + row[2] + '\t' + row[3])
        elif choice == 5:
            data = dao.readAll()
            # id를 주면서 검색
            print('id \t\t pw \t name \t tel')
            print('-------------------------------------------------')
            for row in data:
                line = row[0] + '\t' + row[1] + '\t' + row[2] + '\t' + row[3]

                print(line)
        else:
            sys.exit(0)