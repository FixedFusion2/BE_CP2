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
        #Check if there are any students in the gradebook before trying to add a grade
        if not self.students:
            print("❌ No students in the gradebook. Add students first.")
            input("Press Enter to continue...")
            return                               

        print("=====================================")
        print("📝 ADD GRADE 📝")
        print("Current Students: ")
        #List all students with their names and IDs to help the user select the correct student to add a grade for
        for s in self.students:
            print(f"- {s.name} (ID: {s.id})")

        #Prompt the user to enter the student ID for the student they want to add a grade for, then find that student in the students list
        student_id = input("Enter the student ID to add a grade: ")
        student = next((s for s in self.students if s.id == student_id), None)
        #If the student ID is not found in the students list, inform the user and return to the main menu
        if not student:
            print("❌ Student ID not found.")
            input("Press Enter to continue...")
            return
        #Try to get a valid grade.
        try:
            grade = float(input("Enter the grade to add (0-100): "))
            if grade < 0 or grade > 100:
                raise ValueError
        #If the user enters an invalid grade (not a number or out of range), inform the user and return to the main menu
        except ValueError:
            print("❌ Invalid grade. Must be 0 and 100.")
            input("Press Enter to continue...")
            return
        #Add the grades to the students record and display it. Then save the updated students list to the CSV file
        student.add_grades(grade)
        self.save_students()
        print(f"✅ Grade added successfully! {student.name} now has {len(student.grades)} grade(s)")
        print(f"Current Average: {student.average_grade():.2f} ({student.letter_grade()})")
        input("Press Enter to continue...")
    
    #View student record function
    def view_student_record(self):
        #Check if there are any students in the gradebook before trying to view a student record
        if not self.students:
            print("❌ No students in the gradebook. Add students first.")
            input("Press Enter to continue...")
            return
        #Prompt the user to enter the student ID for the student they want to view the record for, then find that student in the students list
        student_id = input("Enter the student ID to view record: ")
        student = next((s for s in self.students if s.id == student_id), None)
        #If the student ID is not found in the students list, inform the user and return to the main menu
        if not student:
            print("❌ Student not found.")
            #If the student is found, display their name, ID, grades, average grade, and letter grade. If the student has no grades yet, indicate that as well
        else:
            print("=====================================")
            print(f"📋 RECORD FOR {student.name} 📋")
            #If the student has grades, display them along with the average and letter grade. If not, indicate that there are no grades yet
            if student.grades:
                #Display the grades as a comma-separated list.
                print(f"Grades: {', '.join(str(g) for g in student.grades)}")
                print(f"Average: {student.average_grade():.2f} ({student.letter_grade()})")
            else:
                print("Grades: None yet")
        input("Press Enter to continue...")

        #View all students function
    def view_all_students(self):
        #Check if there are any students in the gradebook before trying to view all students
        if not self.students:
            print("❌ No students yet.")
            input("Press Enter to continue...")
            return
        print("=====================================")
        print("👥 ALL STUDENTS 👥")
        print("┌───────────────────────────────┐")
        print("│ ID    │ Name           │ Avg  │ Grade│")
        print("├───────┼────────────────┼──────┼──────┤")
        #For each student in the students list, display their ID, name, average grade, and letter grade in a formatted table
        for s in self.students:
            avg = s.average_grade()
            letter = s.letter_grade()
            #Format the output to align columns properly.
            print(f"│ {s.id:<5} │ {s.name:<14} │ {avg:<5.2f} │ {letter:^5} │")
        print("└───────────────────────────────┘")
        print(f"\nTotal Students: {len(self.students)}")
        input("Press Enter to continue...")

    #Class summary: overall average
    def class_summary(self):
        #Check if there are any students in the gradebook before trying to view the class summary
        if not self.students:
            print("❌ No students yet.")
            input("Press Enter to continue...")
            return
        #Total Grades is the sum of all grades for all students.
        total_grades = sum(sum(s.grades) for s in self.students)
        #Total Count is the total number of grades for all students. This is calculated by summing the length of the grades list for each student.
        total_count = sum(len(s.grades) for s in self.students)
        #Class Average calculations
        class_avg = total_grades / total_count if total_count > 0 else 0
        print("=====================================")
        print("📊 CLASS SUMMARY 📊")
        print(f"Number of Students: {len(self.students)}")
        print(f"Class Average: {class_avg:.2f}")
        input("Press Enter to continue...")

#Menu Function
def menu(gradebook):
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
            gradebook.add_student()
        elif choice == "2":
            gradebook.add_grade_to_student()
        elif choice == "3":
            gradebook.view_student_record()
        elif choice == "4":
            gradebook.view_all_students()
        elif choice == "5":
            gradebook.class_summary()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")
            input("Press Enter to continue...")
#Check if the script is being run directly (instead of imported as a module), and if so, create a Gradebook instance and start the menu loop
if __name__ == "__main__":
    gradebook = Gradebook("individual_projetcs//grade_book//docs//grades.csv")
    menu(gradebook)
