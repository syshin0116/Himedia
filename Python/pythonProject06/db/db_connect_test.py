import pymysql

try:
    conn = pymysql.connect(
        host= 'localhost',
        port= 3366,
        user= 'root',
        password= '1234',
        db= 'big',
        charset= 'utf8'
    )

    print('1. 연결 성공!!', conn.host_info)

    # 연결된 통로(stream)을 통해, SQL문을 보내보자.
    # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
    cur = conn.cursor()

    # 3. sql문을 보내보자
    sql = 'insert into book values ("5", "hi", "http://www.himidia.com", "hi.png")'
     # 커서로 sql문을 보냄.
    result = cur.execute(sql)
    print('sql문 전송 결과>', result)
    conn.commit() #insert한 것 반영
    conn.close()
except Exception as e:
    print("db 연결 중 에러발생!!")
    print('에러정보>> ', e)