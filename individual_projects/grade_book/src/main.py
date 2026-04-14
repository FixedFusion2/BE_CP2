#TE 2nd Simple Grade Book Main
#Import from helper
from helper import*

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

#Run
if __name__ == "__main__":
    gradebook = Gradebook("individual_projetcs//grade_book//docs//grades.csv")
    menu(gradebook)