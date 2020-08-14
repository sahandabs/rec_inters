import mysql.connector
# vars of db
host="localhost"
user="user"
password="4047"
database="recs"



class dbHlpr:
    def __init__(self):
        # connect to db
        self.dbcon = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
        )
        # create cursor to handle sql queries
        self.dbcursor = self.dbcon.cursor()
    def insrt(self,val,sql):
        #insert data to db
        self.dbcursor.execute(sql, val)
    def cmt(self):
        # commit changes to db
        self.dbcon.commit()
    def slctAndFetch(self):
        # select data from db and fetch it
        self.dbcursor.execute("SELECT * FROM data")
        return self.dbcursor.fetchall()
