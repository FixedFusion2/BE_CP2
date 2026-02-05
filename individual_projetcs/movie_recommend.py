#TE 2nd Movie Recommender
#Import CSV
import csv
#Giant movie list holding the CSV File in the list with separate parts in the dictionary
movies = []
#Load in CSV file into list.
#Open the movies.csv file with utf-8 encoding
with open("movies.csv", newline= "",encoding = "utf-8") as csvfile:
    #Reader is set to csv.DictReader(csvfile)
    reader = csv.reader(csvfile)
    #For each row in the reader, append the row to the movies list.
    for row in reader:
    #Show title, director, genre, rating, length(min), and notable actors.
        movies.append({
            "title": row["title"],
            "director": row["director"],
            "genre": row["genre"],
            "rating": row["rating"],
            "length(min)": row["length(min)"],
            "notable actors": row["notable actors"]
        })

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

def movie_list():
    print(movies)

menu()
