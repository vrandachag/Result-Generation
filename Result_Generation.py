import csv

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
	f = open("student_record.csv","w")
	wt= csv.writer(f)
	choice = 'Y'
	global scholar_number
	while choice.upper() == 'Y':
		student = [] 
		student.append(scholar_number + 1)
		scholar_number = scholar_number + 1
		name = input("Enter name of student:")
		student.append(name)
		father_name = input("Enter father's name:")
		student.append(father_name)
		mother_name = input("Enter mother's name:")
		student.append(mother_name)
		address = input("Enter address:")
		student.append(address)
		mobile_number = input("Enter mobile number:")
		student.append(mobile_number)
		wt.writerow(student)
		choice = input("Want to enter more entries?(Y/N):")
	f.close()

#display student details
def display_student_record():
	print("scholar number, name, father's name, mother's name, address, mobile number")
	with open("student_record.csv",'r') as f:
		r = csv.reader(f)
		for row in r:
			print(row)

#subject code and subject names
def subject_details():
	f = open("subject_details.csv",'w')
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
	print("subject code " + " subject")
	with open("subject_details.csv", "r") as f:
		r = csv.reader(f)
		for row in r:
			print(row)

#student - subject code
def student_subject_details():
	f = open("student_subject_details.csv",'w')
	wt = csv.writer(f)
	student_subject = []
	with open("student_record.csv","r") as f1:
		r= csv.reader(f1)
		for row in r:
			student_subject.append(row[0])
			subjects = []
			while subjects.size() < 5:
				display_subject_details()
				subjects = eval(input("Enter list of subject code:"))
				if subjects.size() != 5:
					print("Please enter 5 subjects")
				else:
					student_subject.append(subjects)
					wt.writerow(student_subject)
	f.close()

# display student and the subjects enrolled
def display_student_subject_details():
	print("scholar number, subject code, marks, subject code, marks, subject code, marks, subject code, marks, subject code, marks")
	with open("student_subject_details.csv",'r') as f:
		r = csv.reader(f)
		for row in r:
			print(row)

def student_marks():
	f = open("student_subject_details.csv", "w")
	wt = csv.writer(f)
	with open("student_record.csv", 'r') as f1:
		r = csv.reader(f1)
		for row in r:
			student_marks = []
			student_marks.append(row[0])
			term = input("Enter term:")
			student_marks.append(term)
			year = input("Enter year:")
			student_marks.append(year)
			for i in range(0,5):
				student_marks.append(row[i])
				marks = input("Enter marks of " + row[i] + ":")
				student_marks.append(marks)
			wt.writerow(student_marks)
	f.close()

#to calculate result term-wise
def Result_calc():
	f = open("student_result.csv", 'w')
	wt = csv.writer(f)
	with open("student_subject_details.csv", 'r')as f1:
		r = csv.reader(f1)
		for row in r:
			result = []
			result.append(row[0])
			result.append(row[1])
			result.append(row[2])
			avg = 0
			i=4
			while i<13:
				avg = avg + int(row[i])
				i = i + 2
			avg = avg/5
			result.append(avg)
		wt.writerow(result)
	f.close()

while 1:
	print('\n')
