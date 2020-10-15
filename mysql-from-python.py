import os
import pymysql

username=os.getenv('c9_user')
connection = pymysql.connect(host='localhost',user='root',password='', db='Chinook')

# try:
#     with connection.cursor() as cursor:
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                         Friends(name char(20), age int, DOB datetime); """)
# finally:
#     connection.close()

try:
    with connection.cursor() as cursor:
        rows = [("bob", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
        print(cursor.rowcount, "record(s) affected")
finally:
     connection.close()


