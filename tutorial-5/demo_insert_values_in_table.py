import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="interview_bot"
)

mycursor = mydb.cursor()

sql = "INSERT INTO program_question_answer (program_type, question, answer, question_type) VALUES (%s, %s, %s, %s)"
val = ("r", """What are the different data structures in R? 
               A) Vector, List, Matrix, Dataframe 
               B) List
               C) Matrix
               D) Dataframe""", "A", "easy")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")