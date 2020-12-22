import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="interview_bot"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM program_question_answer")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)