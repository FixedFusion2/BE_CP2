#Import CSV
import csv
from time_handling import current_datetime

#Update Document Variable
#Notes: Save changes to file
print("\n---Document Editor---")
document = input("\nEnter the exact file path for your document: ")

#Def Count Word Function
def count_words(document):
    #Try
    try:
        #Open the document in read mode
        with open(document, 'r') as file:
            #Find the length as a string and break it into words with split
            return len(file.read().split())
    #Except file not found error tell the user that, file couldn't be counted,.
    except FileNotFoundError:
        print("Couldn't count words on file.")

#View Document Function
#Notes: Use r mode to read the file, but not add anything to it.
def view_content(document):
    #Show the current file by opening the file and putting it in read mode and printing the read file
    print("Document Content:")
    with open(document, 'r') as file:
        readed = file.read()
        print(f"\n{readed}\n")
#Add Content to Document Function
#Notes: Use a mode to append and r mode to read the updated document info.
def add_content(document):
    #Set content to a user input asking what you want to write.
    content = input("\nWrite the content you want on the file: ")
    #Open the file and append
    with open(document, 'a') as file:
        file.write(f"\n{content}")
        file.write(f"\nWord Count: {count_words(document)}")
        file.write(f"\nTime Stamp: {current_datetime}\n")
    print("Content added.\n")

#Main Function
def main(document):
    #While Loop
    while True:
        #1. View Document
        print("1. View Document")
        #2. Add Content to Document
        print("2. Add Content to Document.")
        #3. Exit
        print("3. Exit")
        #choice is set to a user input asking for them to choose 1-4.
        choice = input("Choose 1-3: ")
        #Elif choice is set to 2
        if choice == "1":
            #Run View Document
            view_content(document)
        #Elif choice is set to 3
        elif choice == "2":
            #Run Add Content to Document
            add_content(document)
        #Elif choice is set to 4
        elif choice == "3":
            #Print Exiting...
            print('Exiting...')
            #Break
            break
