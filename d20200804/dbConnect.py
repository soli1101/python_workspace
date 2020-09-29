import cx_Oracle

class dbConnect:
    def __init__(self, host, dbname, user, password, port=1521):
        self.host = host
        self.port = port
        self.user = user
        self.dbname = dbname
        self.password = password
        self.connection = cx_Oracle.connect(self.user,self.password,self.host+":"+self.port+"/"+self.dbname)
        print(self.connection)

    def execute(self,sql):
        self.sql = sql
        cur = self.connection.cursor()
        cur.execute(sql)
        resultList = []
        for x in cur:
            resultList.append(x)
        self.connection.close()
        return resultList

if __name__=="__main__":
    db = dbConnect("192.168.0.68","orcl","scott","tiger","1521")
    print(db.execute("Select * from dept"))