#TE 2nd Random Password Generator
#OVERVIEW:
"""Create a program that allows a user to specify password requirements (length, upper/lowercase letters, numbers, and special characters) 
then gives them 4 possible passwords they could use.
"""
#Import Random Module
import random

#Numbers list
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#Upper Letters List
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Lower Letters List
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Special Characters List
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
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
    elif option == "2":
        print("Exiting the program.")
        exit()
    #ELSE
    else:
        #Exit the program
        print("Invalid choice.")
        menu()
        


#RANDOM PASSWORD
def generate_passwords():
    #Length is set to a user input that asks how long the password should be.
    length = int(input("Enter the desired password length: "))
    #lowercase is set to a user input asking them if they want their password to include lowercase letters.
    userlower = input("Include lowercase letters? (y/n): ").lower() == "y"
    #numbers is set to a user input asking them if they want their password to include numbers.
    #uppercase is set to a user input asking them if they want their password to include uppercase letters.
    useupper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    #special characters is set to a user input asking them if they want their password to include special characters.
    use_special = input("Include special characters? (y/n): ").lower() == "y"

    #all characters list
    all_characters = []
    #required characters list
    required_characters = []
    if userlower:
        #Add lowercase letters to all characters and ensure at least one is included
        all_characters.extend(lower_letters)
        required_characters.append(random.choice(lower_letters))
    if useupper:
        #Add uppercase letters to all characters and ensure at least one is included
        all_characters.extend(upper_letters)
        required_characters.append(random.choice(upper_letters))
    if use_numbers:
        #Add numbers to all characters and ensure at least one is included
        all_characters.extend(numbers_list)
        required_characters.append(random.choice(numbers_list))
    if use_special:
        #Add special characters to all characters and ensure at least one is included
        all_characters.extend(special_chars)
        required_characters.append(random.choice(special_chars))
    #Validation checks
    if not all_characters:
        print("Error: You must select at least one character type.")
        return
    if length < len(required_characters):
        print(f"Error: Password length must be at least {len(required_characters)} to include all selected character types.")
        return

    print("Here are your random passwords:")
    #Generate 4 random passwords
    #For loop to generate 4 passwords                                                                       
    for _ in range(4):
        #Password list
        password = required_characters[:]
        #Fill the rest of the password length with random choices from all characters
        for _ in range(length - len(required_characters)):
            #Add random character to password
            password.append(random.choice(all_characters))
            #Shuffle the password to ensure randomness
        random.shuffle(password)
        #Print the password as a string
        print("".join(password))
#Run menu
menu()