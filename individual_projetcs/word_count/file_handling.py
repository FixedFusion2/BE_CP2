#Import CSV
import csv

#Update Document Info Function
#Notes: Save changes to file
def update_document():
    document = input("Enter the exact file path for your document: ")

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
    print("Content added.")