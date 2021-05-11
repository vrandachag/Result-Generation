import mysql.connector
from prettytable import PrettyTable

def Result_Display():
    global mydb
    mycursor = mydb.cursor()

    sql = " SELECT \
    student_details.student_name,student_marks.scholar_number,student_marks.subject_code,subjects.subject_name, student_marks.marks_obtained, student_marks.max_marks,student_marks.class, student_marks.term, student_marks.year \
    FROM student_details \
    JOIN student_marks \
    ON student_marks.scholar_number = %s AND student_marks.term = %s AND student_details.scholar_number = student_marks.scholar_number \
    JOIN subjects \
    WHERE student_marks.subject_code = subjects.subject_code" 

    sn = 1
    term = 4
    t = []
    t.append(str(sn))
    t.append(str(term))
    sn_t = tuple(t)
                        
    mycursor.execute(sql,sn_t)

    myresult = mycursor.fetchall()

    flag = 0
    total = 0
    count = 0
    avg = 0
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

        avg = avg + x[4]
        total = total + x[5]
        count = count + 1

        myTable.add_row(l)

    print(myTable)
    avg = avg/count
    print("Average:" + str(avg))

def Marks_insert():
    global mydb
    mycursor = mydb.cursor()

    subject = input("Enter subject:")
    term = input("Enter term:")
    yr = input("Enter year:")
    s_class = input("Enter class:")
    max_marks = input("Input enter maximum marks:")

    sql = f" SELECT subjects.subject_code \
    FROM subjects \
    WHERE subjects.subject_name = {subject}" 

    mycursor.execute(sql)

    marks = mycursor.fetchall()
    
    for i in marks:
        sql1 = f"SELECT student_details.scholar_number,student_details.student_name,student_details.class, \
        student_details.term, student_details.current_s_year, subjects.subject_code \
            FROM subjects \
            WHERE subjects.subject_name = {i[0]} \
            JOIN student_subject_details \
            WHERE student_subject_details.subject_code_1 = subjects.subject_code OR \
                  student_subject_details.subject_code_2 = subjects.subject_code OR \
                  student_subject_details.subject_code_3 = subjects.subject_code OR \
                  student_subject_details.subject_code_4 = subjects.subject_code OR \
                  student_subject_details.subject_code_5 = subjects.subject_code OR \
                  student_subject_details.subject_code_6 = subjects.subject_code"

        mycursor.execute(sql1)

        name = mycursor.fetchall()
        flag = 0
        for m1 in name:
            if flag == 0:
                print("Class:" + m1[2])
                print("Term:" + m1[3])
                print("Year:" + m1[4])
                flag = 1
            print("Scholar Number:" + m1[0])
            print("Name:" + m1[1])
            inp_marks = input("Enter marks:")
            sql2 = f"INSERT INTO student_marks(Scholar_Number,Subject_Code,Marks_obtained,Max_Marks,Department,Section,Term,S_Year,Year) \
                VALUES(m1[0],m1[5],{inp_marks},{max_marks},{dept},{},m1[3])"


    
mydb = mysql.connector.connect(
host = "localhost",
database = "student_record_system",
user = "root",
password = "Helloworld123"
    #    password = input("Enter password:"),
)
Result_Display()
mydb.close()
