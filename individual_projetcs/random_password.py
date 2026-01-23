#TE 2nd Random Password Generator
#OVERVIEW:
"""Create a program that allows a user to specify password requirements (length, upper/lowercase letters, numbers, and special characters) 
then gives them 4 possible passwords they could use.
"""

#Numbers list
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#Upper Letters List
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Lower Letters List
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Special Characters List
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
#MENU
def menu():
    #Display
    print("Random Password Generator")
    print("1. Generate Passwords")
    print("2. Exit")
    option = input("Select an option: ")
    if option == "1":
        #Run password generation function
        generate_passwords()
    #ELSE
    else:
        #Exit the program
        print("Exiting the program.")
        exit()


#RANDOM PASSWORD
def generate_passwords():
    #Length is set to a user input that asks how long the password should be.
    length = int(input("Enter the desired password length: "))
    #lowercase is set to a user input asking them if they want their password to include lowercase letters.
    lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    #uppercase is set to a user input asking them if they want their password to include uppercase letters.
    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    #numbers is set to a user input asking them if they want their password to include numbers.
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    #special characters is set to a user input asking them if they want their password to include special characters.
    special_characters = input("Include special characters? (y/n): ").lower() == "y"