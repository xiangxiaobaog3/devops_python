
import pymysql


class check_mysql_slave:
    def __init__(self):
        self.dbhost = "192.168.128.92"
        self.dbuser = 'exporter'
        self.dbpass = '123456'
        self.dbport = 3306


    def run_scheduler(self):
        db = pymysql.connect(host=self.dbhost, user=self.dbuser, password=self.dbpass)
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchall()
        print("Database version : %s " % data)
        db.close()

check_mysql_slave().run_scheduler()
