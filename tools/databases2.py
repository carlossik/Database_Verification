import MySQLdb

class sqlserver(object):

    def __init__ (self, host, userid, pwd, database):
        self.host = host
        self.userid = userid
        self.pwd = pwd
        self.db = database

    def GetDataStore(self, sql):
        conn = MySQLdb.connect(host=self.host, user=self.userid, password=self.pwd, database=self.db)
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()
        for row in rows:
            print(rows)





myconnection = sqlserver("proteus.odin.tel-dev.io","root","tli00eNND2ROLm:d,cq-","dspe")


Status =  myconnection.GetDataStore("select status from dspe.etl_job_control where job_id = 101163;")
