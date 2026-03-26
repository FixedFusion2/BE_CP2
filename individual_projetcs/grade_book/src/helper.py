#TE 2nd Helper Functions for Simple Gradebook

#Student Class
class Student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades


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
#View Student Record Function
#View All Students Function
#Class Summary Function
