import csv
from tkinter import *
from prettytable import PrettyTable

scholar_number = 0

#read complete file and then initialize
def scholar_number_init():
        global scholar_number
        scholar_number = 0
        with open("student_record.csv","r") as f:
                r= csv.reader(f)
                for row in r:
                        scholar_number = scholar_number + 1
        if(scholar_number == 0):
                print("File is empty")

#basic details of student (master file)
def student_record():
      #  window1.withdraw()
        window = Tk()
        window.geometry("1000x600")

        window.title("Student Record")
        f = open("student_record.csv","a")
        wt= csv.writer(f)
        choice = 'Y'
        global scholar_number
        while choice.upper() == 'Y':
                student = []
                student.append(scholar_number + 1)
                scholar_number = scholar_number + 1
                n1 = Label(window,
                           text = "Enter name:",
                           font = "Georgia",
                           justify = LEFT)
                n1.grid(row = 0,column = 0)
                name = StringVar()
                n1_e = Entry(window,
                             textvariable = name,
                             font = "Georgia",
                             bg = "white")
                n1_e.grid(padx = 0, pady = 0, row = 0,column = 1)
                student.append(name.get())
                
                f1 = Label(window,
                           text = "Enter Father's name:",
                           font = "Georgia",
                           justify = LEFT)
                f1.grid(padx = 0, pady = 1,row = 1,column = 0)
                father_name = StringVar()
                f1_e = Entry(window,
                             textvariable = father_name,
                             font = ("Georgia"),
                             bg = "white")
                f1_e.grid(padx = 0, pady = 1,row = 1,column = 1)
                student.append(father_name.get())
                
                m1 = Label(window,
                           text = "Enter Mother's name:",
                           font = "Georgia",
                           justify = LEFT)
                m1.grid(padx = 0, pady = 2,row = 2,column = 0)
                mother_name = StringVar()
                m1_e = Entry(window,
                             textvariable = mother_name,
                             font = ("Georgia"),
                             bg = "white")
                m1_e.grid(padx = 0, pady = 2,row = 2,column = 1)
                student.append(mother_name.get())
                
                a1 = Label(window,
                           text = "Enter address:",
                           font = "Georgia",
                           justify = LEFT)
                a1.grid( padx = 0, pady = 3,row = 3,column = 0)
                address = StringVar()
                a1_e = Entry(window,
                             textvariable = address,
                             font = ("Georgia"),
                             bg = "white")
                a1_e.grid(padx = 0, pady = 3,row = 3,column = 1)
                student.append(address.get())
                
                mn = Label(window,
                           text = "Enter Mobile Number:",
                           font = "Georgia",
                           justify = LEFT)
                mn.grid( padx = 0, pady = 4,row = 4,column = 0)
                mobile_number = IntVar()
                mn_e = Entry(window,
                             textvariable = mobile_number,
                             font = ("Georgia"),
                             bg = "white")
                mn_e.grid(padx = 0, pady = 4,row = 4,column = 1)
                student.append(mobile_number.get())
                
                wt.writerow(student)

                option = Label(window,
                               text = "Want to enter more entries?",
                               font = ("Georgia"),
                               justify = LEFT)
                option.grid(padx = 0,pady = 5,row = 6,column = 0)
                
                yes_btn = Button(window,
                                 text = 'Yes', 
                                 command = student_record)
                yes_btn.grid(padx = 0,pady = 5,row = 6,column = 1)
                
                no_btn = Button(window,
                                text = 'No',
                                command = main_menu)
                no_btn.grid(padx = 0,pady = 5,row = 6,column = 3)

        window.destroy()
        f.close()

#display student details
def display_student_record():
#        window1.withdraw()
        window = Tk()
        window.title("Student Record")
        window.geometry("1000x600")
        i = 1
        with open("student_record.csv",'r') as f:
                r = csv.reader(f)
                myTable = PrettyTable(["Scholar Number","Name","Father's Name","Mother's Name","Address","Mobile Number"])
                for row in r:
                        myTable.add_row([row[0],row[1],row[2],row[3],row[4],row[5]])
                        print(myTable)
                        Label(window,
                              text = myTable,
                              font = "Georgia").grid(row = 0,column = i)
                        i = i + 1

#subject code and subject names
def subject_details():
   #     window1.withdraw()
        window = Tk()
        window.title("Subject Details")
        f = open("subject_details.csv",'a')
        wt = csv.writer(f)
        subject = []
        sc = Label(window,
                   text = "Enter subject code:",
                   font = "Georgia",
                   bg = "white")
        sc.grid(row = 0,column = 0)
        subject_code = StringVar()
        sc_e = Entry(window1,
                     textvariable = subject_code,
                     font = "Georgia",
                     bg = "white")
        sc_e.grid(row = 0,column = 1)
        subject.append(subject_code)
        
        sn = Label(window,
                   text = "Enter subject name:",
                   font = "Georgia",
                   bg = "white")
        sn.grid(row = 1,column = 0)
        subject_name = StringVar()
        sn_e = Entry(window1,
                     textvariable = subject_name,
                     font = "Georgia",
                     bg = "white")
        sn_e.grid(row = 1,column = 1)
        subject.append(subject_name)

        wt.writerow(subject)

        choose.Label(window,
                     text = "Want to enter more entries?(Y/N):",
                     font = ("Georgia"),
                     justify = LEFT)
        choose.grid(padx = 0,pady = 5,row = 2,column = 0) 
        yes_btn = Button(window,
                         text = 'Yes', 
                         command = subject_details)
        yes_btn.grid(padx = 0,pady = 1,row = 2,column = 1)
        no_btn = Button(window,
                        text = 'No',
                        command = main)
        no_btn.grid(padx = 0,pady = 1,row = 2,column = 2)
        window.destroy()

        f.close()

# display subject code and corresponding subject
def display_subject_details():
        window1.withdraw()
        window = Tk()
        window.title("Student Record")
        window.geometry("1000x600")
        i = 1
        with open("subject_details.csv",'r') as f:
                r = csv.reader(f)
                myTable = PrettyTable(["Subject Code","Subject Name"])
                for row in r:
                        myTable.add_row([row[0],row[1]])
                        Label(window,
                              text = myTable,
                              font = "Georgia").grid(row = 0,column = i)
                        i = i + 1
##here
def onclick():
    global click
    c1 = click.get()
    
#student - subject code
def student_subject_details():
    #scholar number, name,subject_code,name
        window = Tk()
        f = open("student_subject_details.csv",'a')
        wt = csv.writer(f)
        with open("student_record.csv","r") as f1:
                r= csv.reader(f1)
                for row in r:
                        student_subject = []
                        detail.Label(window,
                                     text = "\nEnter subjects for " + row[1] + ":",
                                     font = "Georgia")
                        detail.grid(row = 0,column = 0)
                        student_subject.append(row[0])
                        student_subject.append(row[1])
                        global click
                        click = IntVar()
                        with open("subject_details.csv","r") as f2:
                            r1 = csv.reader(f2)
                            i = 0
                            for row1 in r1:
                                Checkbutton(window,
                                            text = row1[1]
                                            variable = click
                                            command = onclick).grid(row=i,column=0)
                                i = i + 1
                                            
'''
                        i = 0
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
                        wt.writerow(student_subject)'''
        f.close()

# display student and the subjects enrolled
def display_student_subject_details():
    window = Tk()
    window.title("Student-Subject Details")
    window.geometry("1000x600")
    with open("student_subject_details.csv",'r') as f:
        r = csv.reader(f)
        myTable = PrettryTable(["scholar number","Name:","Subject Code:","Subject name:","Subject Code:","Subject name:"])
        i = 0
        for row in r:
            myTable.add_row([row[0], row[1],row[2],row[3], row[4],row[5]])
            Label(window,
                  text = myTable,
                  font = "Georgia").grid(row = i,column = 0)
            i = i + 1
            

#To input marks of student
def student_marks():
    window = Tk()
    window.title("Student Marks")
    window.geometry("1000x60")
    f = open("student_marks.csv", "a")
    wt = csv.writer(f)
    with open("student_subject_details.csv", 'r') as f1:
        r = csv.reader(f1)
        t1 = Label(window,
                   text = "Enter term:",
                   font = "Georgia"
                   bg = "white")
        t1.grid(row = 0,column = 0)
        term = IntVar()
        t1_e = Entry(window,
                     textvariable = term,
                     font = "Georgia",
                     bg = "white")
        t1_e.grid(row = 0,column = 1)

        y1 = Label(window,
                   text = "Enter year:",
                   font = "Georgia",
                   bg = "white")
        y1.grid(row = 1,column = 0)
        year = IntVar()
        y1_e = Entry(window,
                     textvariable = year,
                     font = "Georgia",
                     bg = "white")
        y1_e.grid(row= 1,column = 1)
        i = 2
        for row in r:
            student_marks = []
            r2 = Label(window,
                       text = "Enter marks for " + row[1] + ":",
                       font = "Georgia",
                       bg = "white")
            r2.grid(row = i,column = 0)
            i = i + 1
            student_marks.append(row[0])    
            student_marks.append(row[1])            
            student_marks.append(term)
            student_marks.append(year)
            j = 2
            for j in range(2,6):
                if j%2 == 0:
                    student_marks.append(row[j])
                    student_marks.append(row[j+1])
                    m1 = Label(window,
                               text = ("Enter marks of " + row[j+1] + ":"),
                               font = "Georgia",
                               bg = "white")
                    m1.grid(row = i,column = 0)
                    marks = IntVar()
                    m1_e = Entry(window,
                                 textvariable = marks,
                                 font = "Georia",
                                 bg = "white")
                    m1_e.grid(row = i , column = 1)
                    i = i + 1
                    student_marks.append(marks)
                    j = j + 2
            wt.writerow(student_marks)
        f.close()

#display student marks
def display_student_marks():
    window = Tk()
    window.Title("Student Marks")
    window.geometry("1000x600")
    with open("student_marks.csv",'r') as f:
        r = csv.reader(f)
        myTable = PrettyTable(["scholar number","name","subject","marks","subject","marks"])
        for row in r:
            myTable.add_row([row[0],row[1],row[5], row[6], row[8],row[9]])
        Label(window,
              text = myTable,
              font = "Georgia").grid(row= 0,column = 0)

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

def Submit():
        global choice
        choice_1 = choice.get()
   #     choice_1 = 1
        
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

def main_menu():
        window1 = Tk()
        window1.title("Result-Main Menu")
        window1.geometry("1000x600")
        Label(window1,
              text = '\n1. Add Student Details \n2. Display Student Details \n3. Add Subject Details \n4. Display Subject Details \n5. Assign subjects for the students \n6. Display subjects enrolled by the student \n7. To input marks of student \n8. Display Student marks \n9. Display result of the students',
              font = 'Georgia',
              justify = LEFT).grid(padx = 0,row = 0,column = 0)
        global choice
        choice = IntVar()
        c1 = choice.get()
        Entry(window1,
              textvariable = choice,
              font = ("Georgia"),
              fg = "Black",
              bg = "white").grid(padx = 1, pady = 0, row = 1, column = 0)
        sub_btn = Button(window1,
                         text = 'Submit', 
                         command = Submit,
                         fg = "Black",
                         background = "white",
                         font = ("Georgia"))
        sub_btn.grid(padx = 0,pady = 1,row = 2,column = 0)

#def want_to_enter_more():
        
scholar_number_init()
main_menu()
choice = IntVar()
