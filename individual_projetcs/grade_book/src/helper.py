#TE 2nd Helper Functions for Simple Gradebook

#Student Class
import csv


class Student:
    #Constructor to initialize student attributes
    def __init__(self, name, student_id, grades=None):
        self.name = name
        self.id = student_id
        self.grades = grades if grades else []
    #Method to add a grade to the student's record
    def add_grades(self,grade):
        self.grades.append(grade)
    #Method to calculate the average grade for the student
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    #Method to determine the letter grade based on the average grade
    def letter_grade(self):
        avg = self.average_grade()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"                                                          

#Gradebook Class
class Gradebook:
    def __init__(self,csv_file):
        self.csv_file = csv_file
        self.students = []
        self.load_students()

    #Load students from csv file
    def load_students(self):
        #Try to read the CSV file and load student data, if the file does not exist, create it
        try:
            with open(self.csv_file, "r",newline="") as file:
                #Reader object to read the CSV file
                reader = csv.reader(file)
                #For each row in the CSV, create a Student object and add it to the students list
                for row in reader:
                    name = row[0]
                    student_id = row[1]
                    grades =  [float(g) for g in row[2].split(";") if g]
                    self.students.append(Student(name, student_id, grades))
        except FileNotFoundError:
            #CSV does not exsist yet, create it
            with open(self.csv_file, "w", newline="") as file:
                pass

    def save_students(self):
        #Open the CSV file for writing and save the student data
        with open(self.csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            #For student in the students list, write their name, ID, and grades to the CSV file
            for s in self.students:
                grades_str = ";".join(str(g) for g in s.grades)
                writer.writerow([s.name, s.id, grades_str])

    def add_student(self):
        print("=====================================")
        print("➕ ADD NEW STUDENT ➕")
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")

        #Check if student ID already exists
        if any(s.id == student_id for s in self.students):
            print("❌ Student ID already exists. Please try again.")
            input("Press Enter to continue...")
            return
        #Create a new Student object and add it to the students list, then save the updated list to the CSV file
        new_student = Student(name, student_id)
        self.students.append(new_student)
        self.save_students()
        print("✅ Student added successfully!")
        print(f"Name: {name}\nID: {student_id}\nGrades: None yet")
        input("Press Enter to continue...")

    #Add grade to student function
    def add_grade_to_student(self):
        if not self.students:
            print("❌ No students in the gradebook. Add students first.")
            input("Press Enter to continue...")
            return                               

        print("=====================================")
        print("📝 ADD GRADE 📝")
        print("Current Students: ")
        for s in self.students:
            print(f"- {s.name} (ID: {s.id})")

        student_id = input("Enter the student ID to add a grade: ")
        student = next((s for s in self.students if s.id == student_id), None)
        if not student:
            print("❌ Student ID not found.")
            input("Press Enter to continue...")
            return
        
        try:
            
#Menu Function
def menu():
    #While loop to keep going until told to stop
    while True:
        print("=====================================")
        print("📚 SIMPLE GRADE BOOK 📚")
        print("=====================================")
        print("Welcome to the Class Gradebook!")
        print("\n🎯 MAIN MENU:")
        print("[1] Add New Student")
        print("[2] Add Grade to Student")
        print("[3] View Student Record")
        print("[4] View All Students")
        print("[5] Class Summary")
        print("[6] Exit\n")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_new()
        elif choice == "6":
            print("Exiting...")
            break

#Add New Student Function
def add_new():
    print("=====================================")
    print("➕ ADD NEW STUDENT ➕")
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    with open("individual_projetcs\\grade_book\\docs\\grades.csv", "a",newline="") as file:
        file.write(student_name, student_id)
    print("✅ Student added successfully!")
    print(f"Name: {student_name}")
    print(f"ID: {student_id}")
    print("Grades: None yet")
    input("Press Enter to continue..")

#Add Grade to Student Function
def add_grade():
    print("Add Grades")
#View Student Record Function
#View All Students Function
#Class Summary Function
