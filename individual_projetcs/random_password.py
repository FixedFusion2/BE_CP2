#TE 2nd Random Password Generator
#OVERVIEW:
"""Create a program that allows a user to specify password requirements (length, upper/lowercase letters, numbers, and special characters) 
then gives them 4 possible passwords they could use.
"""
#Import Random Module
import random

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
    #If lowercase is yes have lowercase = True
    if lowercase == "y":
        lowercase = True
    else:
        #Else False
        lowercase = False
    #uppercase is set to a user input asking them if they want their password to include uppercase letters.
    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    #If uppercase is yes have uppercase = True
    if uppercase == "y":
        uppercase = True
    else:
        #Else False
        uppercase = False
    #numbers is set to a user input asking them if they want their password to include numbers.
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    #If numbers is yes have numbers = True
    if numbers == "y":
        numbers = True
    else:
        #Else False
        numbers = False
    #special characters is set to a user input asking them if they want their password to include special characters.
    special_characters = input("Include special characters? (y/n): ").lower() == "y"
    #If special characters is yes have special_characters = True
    if special_characters == "y":
        special_characters = True
    else:
        #Else False
        special_characters = False
    #Create an empty list to hold all possible characters
    all_characters = []
    if lowercase:
        all_characters.extend(lower_letters)
    if uppercase:
        all_characters.extend(upper_letters)
    if numbers:
        all_characters.extend(numbers)
    if special_characters:
        all_characters.extend(special_characters)

    #Check if the user has selected at least one character type
    if not all_characters:
        print("Error: You must select at least one character type.")
        return

    #Generate 4 random passwords
    passwords = []
    for _ in range(4):
        password = ''.join(random.choice(all_characters) for _ in range(length))
        passwords.append(password)

    #Display the generated passwords
    print("Here are your random passwords:")
    for pwd in passwords:
        print(pwd)

menu()