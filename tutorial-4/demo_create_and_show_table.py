import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="interview_bot"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE program_question_answer (program_type VARCHAR(255), question VARCHAR(255), answer VARCHAR(255), question_type VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)