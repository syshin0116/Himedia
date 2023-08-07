import pymysql

# data access module
# crud기능
# def 4개 필요!



# def create(id, name, url, img):
def create(vo):
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'insert into book values (%s, %s, %s, %s)'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, vo)
        print('sql문 전송 결과>', result)
        conn.commit()  # insert한 것 반영
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)


def read(id):
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'select * from book where id = %s'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, id)
        # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다
        row = cur.fetchone() #row하나만 꺼내
        return row
        print(row)
        print('sql문 전송 결과>', result)
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)
def readAll():
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'select * from book'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql)
        # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다
        row = cur.fetchall() #row하나만 꺼내
        return row
        print(row)
        print('sql문 전송 결과>', result)
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)


def update(vo):
    id, name, url, img = vo
    vo = (name, url, img, id)
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'update book set name = %s, urls = %s, img = %s where id = %s' #%(name, url, img, id)
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, vo)
        print('sql문 전송 결과>', result)
        conn.commit()  # update한 것 반영
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)

def delete(vo):
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'delete from book where id = %s'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, vo)
        print('sql문 전송 결과>', result)
        conn.commit()  # update한 것 반영
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)

