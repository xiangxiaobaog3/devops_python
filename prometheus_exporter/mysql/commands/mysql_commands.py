
import pymysql


class check_mysql:
    def __init__(self):
        self.dbhost = "192.168.128.92"
        self.dbuser = 'exporter'
        self.dbpass = '123456'
        self.dbport = 3306


    def slave_status(self):
        db = pymysql.connect(host=self.dbhost, user=self.dbuser, password=self.dbpass)
        cursor = db.cursor()
        cursor.execute("show slave status")
        data = cursor.fetchall()
        slave_io = data[0][11]
        slave_sql = data[0][12]
        db.close()

        if slave_io == 'Yes' or slave_sql == 'Yes':
            return 1
        else:
            return 0


if __name__ == "__main__":
    check_mysql().slave_status()