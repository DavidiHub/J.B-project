import mysql.connector

class DAL:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='davidi1231', database='mydb')


    def get_table(self, sql:str):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            table = cursor.fetchall()
            return table

    def get_one(self, sql, parmas=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, parmas)
            one = cursor.fetchone()
            return one
        
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            last_row_id = cursor.lastrowid
            return last_row_id
        
    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count
        
    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count

        
    def close(self):
        self.connection.close()