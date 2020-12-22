import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE interview_bot")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x) 