import cx_Oracle

# 1. connection 객체 생성
connection = cx_Oracle.connect("scott","tigertiger","orcl.cz38wovdwt3h.ap-northeast-2.rds.amazonaws.com:1521/orcl")

# 2. cur 객체 생성 
cur = connection.cursor()       

# 3. sql문 객체 생성
sql = '''
        INSERT INTO dept 
        VALUES(:deptno, :dname, :loc)'''
sql2 = '''
        INSERT INTO dept(deptno, loc)
        VALUES(:deptno, :loc)'''

# 4. cur 실행문 작성
cur.execute(sql2,[3,"INCHEON"])
connection.commit()

# 5. 로직처리 및 출력하기
print(connection)

# 6. 자원반납하기