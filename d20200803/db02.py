import cx_Oracle
# 1. connection 객체 생성
connection = cx_Oracle.connect("scott", "tigertiger","orcl.cz38wovdwt3h.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)

# 2. cursor 객체 생성
cur = connection.cursor()

# 3. 사용할 sql문 객체
sql = '''
SELECT empno, ename, sal
FROM emp
WHERE ename = :txt
'''

# 4. 실행
cur.execute(sql,txt="SCOTT")
print(cur)

# 5. 로직처리
for empno, ename, sal in cur:
    print("{} \t {} \t {}".format(empno,ename,sal))

# 6. 자원반납
connection.close() # 내부적으로 사용했던 자원 반납