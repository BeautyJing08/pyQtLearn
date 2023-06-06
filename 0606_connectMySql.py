# 現在要用這個連線看看mysql
import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password = "5321",
    database = "sql_tutorial"

)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM member_table")

result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
mydb.close()

