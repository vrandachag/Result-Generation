import csv
from tkinter import *

scholar_number = 0

#read complete file and then initialize
def scholar_number_init():
        global scholar_number
        with open("student_record.csv","r") as f:
                r= csv.reader(f)
                for row in r:
                        scholar_number = scholar_number + 1

#basic details of student (master file)
def student_record():
        window = Tk()
        window.title("Student Record")
        f = open("student_record.csv","a")
        wt= csv.writer(f)
        choice = 'Y'
        global scholar_number
        while choice.upper() == 'Y':
                student = []
                student.append(scholar_number + 1)
                scholar_number = scholar_number + 1
                Label(window,
                      text = "Enter name:",
                      font = "Georgia",
                      justify = LEFT).grid(padx = 0, pady = 0)
                name = StringVar()
                Entry(window,
                      textvariable = name,
                      font = "Georgia",
                      bg = "blue").grid(padx = 0, pady = 1, row = 1,column = 0)
                student.append(name)
                
                Label(window,
                      text = "Enter Father's name:",
                      font = "Georgia",
                      justify = LEFT).grid(padx = 0, pady = 1)
                father_name = StringVar()
                Entry(window,
                      textvariable = father_name,
                      font = ("Georgia"),
                      bg = "white").grid(padx = 0, pady = 1,row = 1,column = 1)
                student.append(father_name)
                
                Label(window,
                      text = "Enter Mother's name:",
                      font = "Georgia",
                      justify = LEFT).grid(padx = 0, pady = 2)
                mother_name = StringVar()
                Entry(window,
                      textvariable = mother_name,
                      font = ("Georgia"),
                      bg = "white").grid(padx = 0, pady = 2,row = 2,column = 1)
                student.append(mother_name)
                
                Label(window,
                      text = "Enter address:",
                      font = "Georgia",
                      justify = LEFT).grid( padx = 0, pady = 3)
                address = StringVar()
                Entry(window,
                      textvariable = address,
                      font = ("Georgia"),
                      bg = "white").grid(padx = 0, pady = 3,row = 3,column = 1)
                student.append(address)
                
                Label(window,
                      text = "Enter Mobile Number:",
                      font = "Georgia",
                      justify = LEFT).grid( padx = 0, pady = 4)
                mobile_number = IntVar()
                Entry(window,
                      textvariable = mobile_number,
                      font = ("Georgia"),
                      bg = "white").grid(padx = 0, pady = 4,row = 4,column = 1)
                student.append(mobile_number)
                
                wt.writerow(student)
                Label(window,
                      text = "Want to enter more entries?(Y/N):",
                      font = ("Georgia"),
                      justify = LEFT).grid(padx = 0,pady = 5,row = 5,column = 0) 
                Button(window,
                       text = 'Yes', 
                       command = student_record).grid(padx = 0,pady = 1,row = 1,column = 1)
                Button(window,
                       text = 'No',
                       command = main).grid(padx = 0,pady = 1,row = 1,column = 2)
        f.close()

#display student details
def display_student_record():
        with open("student_record.csv",'r') as f:
                r = csv.reader(f)
                for row in r:
                        print("\n")
                        print("Scholar number:" + row[0])
                        print("Name:"+ row[1])
                        print("Father's name:" + row[2])
                        print("Mother's name:" + row[3])
                        print("Address:" + row[4])
                        print("Mobile number:" + row[5])

#subject code and subject names
def subject_details():
        f = open("subject_details.csv",'a')
        wt = csv.writer(f)
        choice = 'Y'
        while choice.upper() == 'Y':
                subject = []
                subject_code = input("Enter subject code:")
                subject.append(subject_code)
                subject_name = input("Enter subject name:")
                subject.append(subject_name)
                wt.writerow(subject)
                choice = input("Want to enter more entries?(Y/N):")
        f.close()

# display subject code and corresponding subject
def display_subject_details():
        with open("subject_details.csv", "r") as f:
                r = csv.reader(f)
                for row in r:
                        print("\n")
                        print("subject code:" + row[0])
                        print("subject name:" + row[1])

#student - subject code
def student_subject_details():
        window = Tk()
        f = open("student_subject_details.csv",'a')
        wt = csv.writer(f)
        with open("student_record.csv","r") as f1:
                r= csv.reader(f1)
                for row in r:
                        student_subject = []
                        print("\nEnter subjects for " + row[1] + ":")
                        student_subject.append(row[0])
                        student_subject.append(row[1])
                        i = 0
                        display_subject_details()
                        for i in range (0,2):
                                subject_code = input("Enter subject code:")
                                if subject_code not in student_subject:
                                        student_subject.append(subject_code)
                                        with open("subject_details.csv",'r') as f2:
                                                r1 = csv.reader(f2)
                                                for row_1 in r1:
                                                        if row_1[0] == subject_code:
                                                                student_subject.append(row_1[1])
                                                                break
                                                else:
                                                        print("subject not found")
                                        i = i + 1
                        wt.writerow(student_subject)
        f.close()

# display student and the subjects enrolled
def display_student_subject_details():
        with open("student_subject_details.csv",'r') as f:
                r = csv.reader(f)
                for row in r:
                        print("\n")
                        print("scholar number" + row[0])
                        print("Name:" + row[1])
                        print("Subject Code:" + row[2])
                        print("Subject name:" + row[3])
                        print("Subject Code:" + row[4])
                        print("Subject name:" + row[5])

#To input marks of student
def student_marks():
        f = open("student_marks.csv", "a")
        wt = csv.writer(f)
        with open("student_subject_details.csv", 'r') as f1:
                r = csv.reader(f1)
                term = input("Enter term:")
                year = input("Enter year:")
                for row in r:
                        student_marks = []
                        print("\nEnter marks for " + row[1] + ":")
                        student_marks.append(row[0])    
                        student_marks.append(row[1])            
                        student_marks.append(term)
                        student_marks.append(year)
                        for i in range(2,6):
                                if i%2 == 0:
                                        student_marks.append(row[i])
                                        student_marks.append(row[i+1])
                                        marks = input("Enter marks of " + row[i+1] + ":")
                                        student_marks.append(marks)
                                        i = i + 2
                        wt.writerow(student_marks)
        f.close()

#display student marks
def display_student_marks():
        with open("student_marks.csv",'r') as f:
                r = csv.reader(f)
                for row in r:
                        print("\n")
                        print("scholar number:" + row[0])
                        print("name:" + row[1])
                        print("subject:" + row[5] + "\tmarks:" + row[6])
                        print("subject:" + row[8] + "\tmarks:" + row[9])

#to calculate result term-wise
def Result_calc():
        #max marks grade
        #1,Vranda,2,2,CS3CO10,TOC,88,CS3CO28,DC,90
        with open("student_marks.csv", 'r')as f1:
                r = csv.reader(f1)
                print("term:" + r[2])
                print("Year:" + r[3])
                for row in r:
                        print("\nScholar number:" + row[0])
                        print("Name:" + row[1])
                        avg = 0
                        percentage = 0
                        i=5
                        while i<10:
                                print("Marks in " + row[i] + " is:" + row[i+1])
                                avg = avg + int(row[i+1])
                                i = i + 3
                        percentage = avg * 0.5                  
                        print("Total Marks:" + str(avg))
                        print("Total percentage:" + str(percentage))

def Submit(choice):
        choice_1 = choice.get()
        if choice_1 == 1:
                student_record()
        elif choice_1 == 2:
                display_student_record()
        elif choice_1 == 3:
                subject_details()
        elif choice_1 == 4:
                display_subject_details()
        elif choice_1 == 5:
                student_subject_details()
        elif choice_1 == 6:
                display_student_subject_details()
        elif choice_1 == 7:
                student_marks()
        elif choice_1 == 8:
                display_student_marks()
        else:
                Result_calc()
        Label(window1,
              text = '\nWant to enter more?(Y or N):',
              font = 'Georgia').grid(padx = 1,pady = 0)
        val = Entry(window1).grid(padx = 1,pady = 1)
#        if val.upper() == 'N':

def main():
        window1 = Tk()
        window1.title("Result-Main Menu")
        scholar_number_init()
        Label(window1,
              text = '\n1. Add Student Details \n2. Display Student Details \n3. Add Subject Details \n4. Display Subject Details \n5. Assign subjects for the students \n6. Display subjects enrolled by the student \n7. To input marks of student \n8. Display Student marks \n9. Display result of the students',
              font = 'Georgia',
              justify = LEFT).grid(padx = 0)
        choice = IntVar()
        c1 = Entry(window1,
                   textvariable = choice,
                   font = ("Georgia"),
                   fg = "blue",
                   bg = "white").grid(padx = 1, pady = 0, row = 1, column = 0)
        sub_btn = Button(window1,
                         text = 'Submit', 
                         command = Submit(choice),
                         fg = "white",
                         background = "red",
                         font = ("Georgia")).grid(padx = 0,pady = 1,row = 2,column = 2)

main()
