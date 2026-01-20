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
def add_book():
        #Print prompt to add books to the library
        print("\nAdd a book to your library.")
        #Add book is set to an input to enter a book title.
        title = input("\nEnter book title: ").strip().title()
        author = input("Enter author: ").strip().title()
        if title == "" or author == "":
            print("\nBook title and author cannot be empty.")
            return
        #Add book to library catalog
        library_catalog.append({'title': title, 'author': author})
        #Print that the book has been added to your library
        print(f"\n'{title}' by {author} has been added to your library.")

#Function to search the items
def search_book():
    if not library_catalog:
        print("\nYour library is empty. Please add books first.")
        return
    #Print prompt to search for a book in the library
    print("\nWhat would you like to search by?")
    print("1. Title")
    print("2. Author")
    search_choice = input("\nEnter your choice: ")
    if search_choice == "1":
        search_term = input("\nEnter book title: ").strip().title()
        found = False
        for book in library_catalog:
            if book['title'] == search_term:
                print(f"\n'{book['title']}' by {book['author']} is in your library.")
                found = True
                break
        if not found:
            print(f"\n'{search_term}' is not in your library.")
    elif search_choice == "2":
        search_term = input("\nEnter author: ").strip().title()
        found = False
        for book in library_catalog:
            if book['author'] == search_term:
                print(f"\n'{book['title']}' by {book['author']} is in your library.")
                found = True
                break
        if not found:
            print(f"\n'{search_term}' is not in your library.")
    else:
        print("Invalid choice. Please try again.")
        return
#Function to remove an item
def remove_book():
    if not library_catalog:
        print("\nYour library is empty. Please add books first.")
        return
    #Print prompt to remove a book from the library
    print("\nRemove a book from your library.")
    #Remove book is set to an input to enter a book title.
    title= input("\nEnter book title: ").strip().title()
    #Check if the book is in the library catalog
    for book in library_catalog:
        if book['title'] == title:
            library_catalog.remove(book)
            print(f"\n'{title}' has been removed from your library.")
            return
    print(f"\n'{title}' is not in your library.")       
#View Function
def view_books():
    #Print all books in the library
    print("\nYour library contains the following books:")
    if not library_catalog:
        print("No books found.")
    else:
        for book in library_catalog:
            print(f"'{book['title']}' by {book['author']}")

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
        menu_choice = input("\nEnter your choice: ").strip()
        #Call the appropriate function based on user choice
        #If 1, add books
        if menu_choice == "1":
            add_book()
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
            print("Invalid choice. Please enter a number between 1 and 5.")
    
#Call the menu function again to display the options
menu()
