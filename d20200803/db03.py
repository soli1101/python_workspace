import cx_Oracle

# 1. connection 객체 생성
connection = cx_Oracle.connect("scott","tigertiger","orcl.cz38wovdwt3h.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)           

# 2. cur 객체 생성 
cur = connection.cursor()       

# 3. sql문 객체 생성
sql = '''                       
Select empno, ename, job, deptno 
From emp
Where deptno = 10'''

# 4. cur 실행문 작성
cur.execute(sql)

# 5. 로직처리 및 출력하기
for empno, ename, job, deptno in cur:
    print('{}\t{}\t{}\t{}'.format(empno, ename, job, deptno))

# 6. 자원반납하기
connection.close()