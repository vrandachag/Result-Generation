import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    database = "student_record_system",
    user = "root",
    password = input("Enter password:"),
    )

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

sql = "INSERT INTO student_marks(Scholar_Number,Subject_Code,Marks_obtained,Max_Marks,Class,Term,Year) VALUES(%s,%s,%s,%s,%s,%s,%s)"
val = (
    input("Enter scholar number:"),
    input("Enter Subject code:"),
    input("Enter Marks Obtained:"),
    input("Enter Max Marks:"),
    input("Enter Class:"),
    input("Enter term:"),
    input("Enter year:")
    )
mycursor.execute(sql,val)
mydb.commit()

mydb.close()
