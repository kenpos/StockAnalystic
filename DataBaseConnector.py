import mysql.connector

class DBControl:
    cursor =""
    conn=""
    def connect(self,host,user,password):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.cursor.close()
        self.conn.close()

    def control(self,comand):
        # self.cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        self.cursor.execute(comand)
