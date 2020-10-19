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

# try:
#     with connection.cursor() as cursor:
#         rows = [("bob", 21, "1990-02-06 23:04:56"),
#                 ("jim", 56, "1955-05-09 13:12:45"),
#                 ("fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
#         connection.commit()
#         print(cursor.rowcount, "record(s) affected")
# finally:
#      connection.close()


# try: 
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:  
#         sql = "select * from Artist limit 5;"
#         cursor.execute(sql)  
#         result = cursor.fetchall() 
#         print(result)

# finally:      	
#     connection.close()

# try:
#     with connection.cursor() as cursor:
        # cursor.execute("CREATE TABLE IF NOT EXISTS Friends(name char(20), age int, DOB datetime);")
        # note the above still display warning 

        # print(cursor.rowcount, "record(s) affected")

# finally:
#     connection.close()

# try: 
#     with connection.cursor() as cursor:
#        ## insert ##
#         rows = [("bob", 21, "1990-02-06 23:04:56"),
#                 ("jim", 56, "1955-05-09 13:12:45"),
#                 ("fred", 100, "1911-09-12 01:01:01")]

#         cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
#         connection.commit()

#         #to test print the python inserts
#         print(cursor.rowcount, "record(s) affected")
#         sql = "select * from Friends;" 
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print (result)

# finally:
#      connection.close()

# try:
#     with connection.cursor() as cursor:
#         #update 1 record
#         sql = "UPDATE Friends SET age = 22 WHERE name = 'bob';"
#         cursor.execute(sql)
#         cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;", (23, 'bob'))
#         connection.commit()
#         print(cursor.rowcount, "record(s) affected")

# finally:
#     connection.close()

# try:
#     with connection.cursor() as cursor:
#         #update many records
#         rows = [(21, 'bob'),
#                 (21, 'jim'),
#                 (21, 'fred')]
#         cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;" , rows)
#         connection.commit()
#         print(cursor.rowcount, "record(s) affected")
# finally:
#      connection.close()

#DELETE
try:
    with connection.cursor() as cursor:
        #sql = "Delete from Friends where name = 'bob'"
        #cursor.execute(sql)
        rows = ['bob', 'jim']
        cursor.executemany("DELETE FROM Friends WHERE name = %s;", rows)
        connection.commit()
        print(cursor.rowcount, "record(s) affected")
finally:
     connection.close()
