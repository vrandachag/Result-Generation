import csv
from tkinter import *
from tkinter import messagebox
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
'''        if(scholar_number == 0):
                print("File is empty")'''


#to append data in file
def submit_student_record(scholar_no,name,fathers_name,mothers_name,address,mobile_number,file_name):
        mno = mobile_number.get()
        student = []
        student.append(scholar_no)
        student.append(name.get())
        student.append(fathers_name.get())
        student.append(mothers_name.get())
        student.append(address.get())
        student.append(mno)
        f = open(file_name,"a", newline='')
        wt = csv.writer(f)
        wt.writerow(student)
        option = messagebox.askquestion("Student Details","Want to enter more entries?")

        if option.upper() == 'YES':      
            student_record()
        else:
          main_menu()

        f.close()

#basic details of student (master file)
def student_record():
        scholar_number_init()
        window = Tk()
        window.geometry("1000x600")
        window.title("Student Record")

        global scholar_number
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
        
        sub_btn = Button(window,
                         text = 'Submit', 
                         command = lambda:submit_student_record(scholar_number,n1_e,f1_e,m1_e,a1_e,mn_e,"student_record.csv"),
                         fg = "Black",
                         background = "white",
                         font = ("Georgia"))
        sub_btn.grid(row = 7,column = 0)
       
#display student details
def display_student_record():
#        window1.withdraw()
        window = Tk()
        window.title("Student Record")
        window.geometry("1000x600")
        myTable = PrettyTable(["Scholar Number","Name","Father's Name","Mother's Name","Address","Mobile Number"])
        with open("student_record.csv",'r') as f:
                r = csv.reader(f)
                for row in r:
                  myTable.add_row([row[0],row[1],row[2],row[3],row[4],row[5]])
                print(myTable)
                Label(window,
                      text = myTable,
                      font = "Georgia").grid(row = 0,column = 0)
                
#subject code and subject names
def subject_details():
   #     window1.withdraw()
        window = Tk()
        window.title("Subject Details")
      #  f = open("subject_details.csv",'a')
       # wt = csv.writer(f)
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

        #wt.writerow(subject)

        sub_btn = Button(window,
                         text = 'Submit', 
                         command = lambda:append_file(subject,"subject_details.csv"),
                         fg = "Black",
                         background = "white",
                         font = ("Georgia"))
        sub_btn.grid(row = 3,column = 0)

        choose.Label(window,
                     text = "Want to enter more entries?(Y/N):",
                     font = ("Georgia"),
                     justify = LEFT)
        choose.grid(padx = 0,pady = 5,row = 4,column = 0) 
        yes_btn = Button(window,
                         text = 'Yes', 
                         command = subject_details)
        yes_btn.grid(padx = 0,pady = 1,row = 4,column = 1)
        no_btn = Button(window,
                        text = 'No',
                        command = main)
        no_btn.grid(padx = 0,pady = 1,row = 4,column = 2)
        window.destroy()

#        f.close()

# display subject code and corresponding subject
def display_subject_details():
        window1.withdraw()
        window = Tk()
        window.title("Student Record")
        window.geometry("1000x600")
#        i = 1
        myTable = PrettyTable(["Subject Code","Subject Name"])

        with open("subject_details.csv",'r') as f:
                r = csv.reader(f)
                for row in r:
                        myTable.add_row([row[0],row[1]])
                Label(window,
                      text = myTable,
                      font = "Georgia").grid(row = 0,column = i)
 #                       i = i + 1
##here
def onclick():
    global click
    c1 = click.get()
    print(c1)
    
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
                                            text = row1[1],
                                            variable = click,
                                            command = onclick).grid(row=i,column=0)
                                i = i + 1
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
                   font = "Georgia",
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


#display student marks
def display_student_marks():
    window = Tk()
    window.title("Student Marks")
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
        window = Tk()
        window.title("Result")
        window.geometry("1000x600")
        with open("student_marks.csv", 'r')as f1:
                r = csv.reader(f1)
                myTable = PrettyTable(["Scholar Number","Name","Term","Year",r[5],r[8],"Total Marks","Percentage"])
                for row in r:
                    avg = 0
                    percentage = 0
                    i=5
                    while i<10:
                            avg = avg + int(row[i+1])
                            i = i + 3
                    percentage = avg * 0.5
                    myTable.add_row([row[0],row[1],row[2], row[3],row[6],row[9]],avg,percetage)
        r1 = Label(window,
                   text = myTable,
                   font = "Georgia")
        r1.grid(row = 0,column = 0)

def Submit(choice):
        choice_1 = choice.get()
        global window1
        window1.withdraw()
 
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
        elif choice_1 == 9:
                Result_calc()
        else:
                print("Wrong choice")

def main_menu():
        global window1
        window1 = Tk()
        window1.title("Result-Main Menu")
        window1.geometry("1000x600")
        Label(window1,
              text = '\n1. Add Student Details \n2. Display Student Details \n3. Add Subject Details \n4. Display Subject Details \n5. Assign subjects for the students \n6. Display subjects enrolled by the student \n7. To input marks of student \n8. Display Student marks \n9. Display result of the students',
              font = 'Georgia',
              justify = LEFT).grid(padx = 0,row = 0,column = 0)
        choice = IntVar()
        Entry(window1,
              textvariable = choice,
              font = ("Georgia"),
              fg = "Black",
              bg = "white").grid(padx = 1, pady = 0, row = 1, column = 0)
        sub_btn = Button(window1,
                         text = 'Submit', 
                         command = lambda:Submit(choice),
                         fg = "Black",
                         background = "white",
                         font = ("Georgia"))
        sub_btn.grid(padx = 0,pady = 1,row = 2,column = 0)
        window1.mainloop()

#def want_to_enter_more():
        
print(scholar_number)
#mobile_number = IntVar()
main_menu()
