import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    database = "student_record_system",
    user = "root",
    password = "Helloworld123"
#    password = input("Enter password:"),
    )

mycursor = mydb.cursor()

sql = " SELECT \
student_marks.scholar_number,student_details.student_name, student_marks.subject_code,subjects.subject_name, student_marks.marks_obtained, student_marks.max_marks,student_marks.class, student_marks.term, student_marks.year \
FROM student_details \
JOIN student_marks \
ON student_marks.scholar_number = %s AND student_marks.term = %s AND student_details.scholar_number = student_marks.scholar_number \
JOIN subjects \
WHERE student_marks.subject_code = subjects.subject_code" 

sn = ("1","4")
                    
mycursor.execute(sql,sn)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mydb.close()
