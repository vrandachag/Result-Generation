import mysql.connector
from prettytable import PrettyTable

#def Result_Display:

mydb = mysql.connector.connect(
    host = "localhost",
    database = "student_record_system",
    user = "root",
    password = "Helloworld123"
#    password = input("Enter password:"),
    )

mycursor = mydb.cursor()

sql = " SELECT \
student_details.student_name,student_marks.scholar_number,student_marks.subject_code,subjects.subject_name, student_marks.marks_obtained, student_marks.max_marks,student_marks.class, student_marks.term, student_marks.year \
FROM student_details \
JOIN student_marks \
ON student_marks.scholar_number = %s AND student_marks.term = %s AND student_details.scholar_number = student_marks.scholar_number \
JOIN subjects \
WHERE student_marks.subject_code = subjects.subject_code" 

sn = ("1","4")
                    
mycursor.execute(sql,sn)

myresult = mycursor.fetchall()

flag = 0
myTable = PrettyTable(["Subject Code","Subject Name","Marks Obtained","Max Marks"])
for x in myresult:
    if flag == 0:
        print("Name:" + x[0])
        print("Enrollment Number:" + str(x[1]))
        print("Class:" + x[6])
        print("Term:" + x[7])
        print("Year:" + x[8])
        flag = -1
    l = []
    l.append(x[2])
    l.append(x[3])
    l.append(x[4])
    l.append(x[5])
    myTable.add_row(l)

print(myTable)
mydb.close()
