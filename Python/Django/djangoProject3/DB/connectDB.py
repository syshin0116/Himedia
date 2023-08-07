import pymysql

def readAll():
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='trip',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'select * from survey'
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

    def read(member_idx):
        try:
            conn = pymysql.connect(
                host='localhost',
                port=3366,
                user='root',
                password='1234',
                db='trip',
                charset='utf8'
            )

            print('1. 연결 성공!!', conn.host_info)

            # 연결된 통로(stream)을 통해, SQL문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
            cur = conn.cursor()

            # 3. sql문을 보내보자
            sql = 'select * from survey where member_idx = %s'
            # 커서로 sql문을 보냄.
            result = cur.execute(sql, member_idx)
            # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다
            row = cur.fetchone()  # row하나만 꺼내
            return row
            print(row)
            print('sql문 전송 결과>', result)
            conn.close()
        except Exception as e:
            print("db 연결 중 에러발생!!")
            print('에러정보>> ', e)

def create(vo):
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='trip',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'insert into surveyResult values (%s, %s, %s, %s, %s, %s)'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, vo)
        print('sql문 전송 결과>', result)
        conn.commit()  # insert한 것 반영
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)

def create(vo):
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='trip',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'insert into member values (%s, %s, %s, %s)'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, vo)
        print('sql문 전송 결과>', result)
        conn.commit()  # insert한 것 반영
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)