#TE 2nd Movie Recommender
#Import CSV
import csv
#Load in CSV file into list.
#Open the movies.csv file
def load_movies():
    movies = []
    try:
        with open("movies.csv", "r") as csvfile:
            #Reader is set to csv.reader(csvfile)
            reader = csv.reader(csvfile)
            #For each row in the reader, append the row to the movies list.
            next(reader)
            for row in reader:
                movies.append(row)
    except FileNotFoundError:
        print("Error: movies.csv file not found.")
    return movies

load_movies()
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
        movie_list()
        #Return to the main menu after printing the full movie list.
        menu()
    #Else If the Menu Choice is 3, call the exit_program function.
    elif menu_choice == "3":
        #Call the exit_program function.    
        exit()
        #Return to the main menu after exiting.
        menu()
    #Else exit program
    else:
        print("Invalid choice. Please select a valid option.")

#def movie_list():
    #Print the full movie list.
    #Print the movie list

#def search for a movie
    #Ask user what they want to search by using choosing filters to apply (enter numbers separated by commas, e.g., 1,3):
    #1. Genre
    #2. Director
    #3. Actor
    #4. Length (min/max)
    #search_by is set to an input asking the user to choose 1-4
    #If search_by contains 1, ask the user to enter a genre to search for.
    #Also If search_by contains 2, ask the user to enter a director to search for.
    #Also If search_by contains 3, ask the user to enter an actor to search for.
    #Also If search_by contains 4, ask the user to enter a minimum and maximum length (in minutes) to search for.
    #Else print invalid choice and return to main menu

