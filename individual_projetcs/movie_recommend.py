#TE 2nd Movie Recommender
#Import CSV
import csv
#Giant movie list holding the CSV File in the list with separate parts in the dictionary
movies = []
#Load in CSV file into list.
#Open the movies.csv file with utf-8 encoding
with open("movies.csv", newline= "", encoding="utf-8") as csvfile:
    #Reader is set to csv.DictReader(csvfile)
    reader = csv.DictReader(csvfile)
    #For row in reader, append row to movies list after converting Length (min) to int
    for row in reader: 
        #Convert Length (min) to int
        row["Length (min)"] = int(row["Length (min)"])
        #Add the row to the movies list
        movies.append(row)

#Main Menu Function
def menu():
    #Print 1. Search/Get Recommendations
    print("1. Search/Get Recommendations")
    #Print 2. Print Full Movie List
    print("2. Print Full Movie List")
    #Print 3. Exit
    print("3. Exit")
    #Menu Choice is set to an input asking the user to choose 1-3.
    menu_choice = input("Please choose an option (1-3): ")
    #If the Menu Choice is 1, call the search_movies function.  
    if menu_choice == "1":
        #Call the search_movies function.
        search_movies()
        #Return to the main menu after searching.
        menu()
    #Else If the Menu Choice is 2, call the print_full_movie_list function.
    elif menu_choice == "2":
        #Call the print_full_movie_list function.
        print_full_movie_list()
        #Return to the main menu after printing the full movie list.
        menu()
    #Else If the Menu Choice is 3, call the exit_program function.
    elif menu_choice == "3":
        #Call the exit_program function.    
        exit_program()
        #Return to the main menu after exiting.
        menu()
    #Else exit program
    else:
        print("Invalid choice. Please select a valid option.")

#Def Search Movies Function
def search_movies():