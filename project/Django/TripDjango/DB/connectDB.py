import pymysql

def getSurvey():
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
        print(row)
        print('sql문 전송 결과>', result)
        conn.close()
        return row

    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)

def getSurveyResult(sessionID):
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
        sql = 'select * from surveyResult where member_idx = %s'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, sessionID)
        # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다
        row = cur.fetchall()  # row하나만 꺼내
        print(row)
        print('sql문 전송 결과>', result)
        conn.close()
        return row

    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)

def insertSurveyResult(sessionID, ractivity, answer_db, rarea_db):
    print("sessionID:", sessionID)
    print("ractivity:", ractivity)
    print("answer_db:", answer_db)
    print("rarea:", rarea_db)
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
        sql = 'INSERT INTO surveyResult (member_idx, surveyResult_recommendation, ' \
              'surveyResult_answers, surveyResult_rarea) VALUES (%s, %s, %s, %s)'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, (sessionID, ractivity, answer_db, rarea_db))
        print('sql문 전송 결과>', result)
        conn.commit()  # insert한 것 반영
        conn.close()
    except Exception as e:
        print("insert db 연결 중 에러발생!!")
        print('에러정보>> ', e)
def deleteSurveyResult(idx):
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
        sql = 'delete from surveyResult where surveyResult_idx = %s'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, idx)
        # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다
        print('delete sql문 전송 결과>', result)
        conn.close()
        return result

    except Exception as e:
        print("delete db 연결 중 에러발생!!")
        print('에러정보>> ', e)