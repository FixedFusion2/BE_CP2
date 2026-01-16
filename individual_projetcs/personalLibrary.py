# TE 2nd Personal Library

#OVERVIEW
"""Create a program that allows user to manage a personal library catalog for any ONE type (books, movies, music, etc). 
The project needs to allow users to add new items, display ALL contents, 
search for a specific item (by title, author/artist/director), remove a book from the library, exit the program. """

#Note: We will be building off this project later on so make sure you do a good job on it! 
#Project must include
#Easy to understand variable and function names
#Pseudocode comments explaining what the code is doing
#Good use of white space to keep items separate and easy to read/find
#Have at least 2 people test your code before submission!


#Stores all items in a list
library_catalog = []
#Function to add a new item
def add_books():
        #Print prompt to add books to the library
        print("\nAdd a book to your library.")
        #Add book is set to an input to enter a book title.
        add_book = input("\nEnter book title: ").title()
        enter_author = input("Enter author: ").title()
        #Add book to library catalog
        library_catalog.append((add_book, enter_author))
        #Print that the book has been added to your library
        print(f"\n'{add_book}' by {enter_author} has been added to your library.")

#Function to search the items
def search_book():
    #Print prompt to search for a book in the library
    print("\nWhat would you like to search by?")
    print("1. Title")
    print("2. Author")
    search_choice = input("\nEnter your choice: ")
    if search_choice == "1":
        print("\nEnter book title: ")
    elif search_choice == "2":
        print("\nEnter author: ")
    #Search book is set to an input to enter a book title.
    search_book = input("\nEnter book title: ").title()
    #Check if the book is in the library catalog
    if search_book in library_catalog:
        #Print that book is in library if in library
        print(f"\n'{search_book}' is in your library.")
    else:
        #Print that book is not in library if not in library
        print(f"\n'{search_book}' is not in your library.")

#Function to remove an item
def remove_book():
    #Print prompt to remove a book from the library
    print("\nRemove a book from your library.")
    #Remove book is set to an input to enter a book title.
    remove_book = input("\nEnter book title: ").title()
    #Check if the book is in the library catalog
    if remove_book in library_catalog:
        #Remove book from library catalog
        library_catalog.remove(remove_book)
        #Print that book has been removed from library
        print(f"\n'{remove_book}' has been removed from your library.")
    else:
        #Print that book is not in library if not in library
        print(f"\n'{remove_book}' is not in your library.")

#View Function
def view_books():
    #Print all books in the library
    print("\nYour library contains the following books:")
    if not library_catalog:
        print("No books found.")
    else:
        for book in library_catalog:
            print(f"- {book}")

#Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
def menu():
    #Print welcome to the personal library.
    print("\nWelcome to the personal library.")
    while True:
        #Print menu options
        #Print 1. Add a book
        print("1. Add a book")
        #Print 2. Search for a book
        print("2. Search for a book")
        #Print 3. Remove a book
        print("3. Remove a book")
        #Print 4. View Books
        print("4. View Books")
        #Print 5. Exit
        print("5. Exit")
        menu_choice = input("\nEnter your choice: ")
        #Call the appropriate function based on user choice
        #If 1, add books
        if menu_choice == "1":
            add_books()
        #If 2, search for books
        elif menu_choice == "2":
            search_book()
        #If 3, remove books
        elif menu_choice == "3":
            remove_book()
        #If 4, view all books
        elif menu_choice == "4":
            view_books()
        #If 5, exit program
        elif menu_choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    
#Call the menu function again to display the options
menu()
