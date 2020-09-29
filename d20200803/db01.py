import cx_Oracle

# print(cx_Oracle.init_oracle_client())

# connection = cx_Oracle.connect("id", "pw", "서버:ip:1521/db명")
connection = cx_Oracle.connect("scott", "tigertiger", "orcl.cz38wovdwt3h.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)

cur = connection.cursor()   # cur 객체를 만들고 
query = "select * from dept"
cur.execute(query)          # cur를 실행해 
for x in cur:
    print(x)

# 연결 끊기 -- 사용 후 db와의 연결을 끊어줘야 함!!
connection.close()