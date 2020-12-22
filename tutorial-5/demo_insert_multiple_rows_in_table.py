import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="interview_bot"
)

mycursor = mydb.cursor()


sql = "INSERT INTO program_question_answer (program_type, question, answer, question_type) VALUES (%s, %s, %s, %s)"
# val = ("r", """What are the different data structures in R? 
#                A) Vector, List, Matrix, Dataframe 
#                B) List
#                C) Matrix
#                D) Dataframe""", "A", "easy")

# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")