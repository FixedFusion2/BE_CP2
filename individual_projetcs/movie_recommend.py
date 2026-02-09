#TE 2nd Movie Recommender
#Import CSV
import csv
#Load in CSV file into list.
#Open the movies.csv file
def load_movies():
    movies = []
    try:
        with open("movies.csv", "r", encoding="utf-8") as csvfile:
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
def menu(movies):
    #While loop to keep the menu running until the user chooses to exit.
    while True:
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
            search_movies(movies)
        #Else If the Menu Choice is 2, call the print_full_movie_list function.
        elif menu_choice == "2":
            #Call the print_full_movie_list function.
            movie_list(movies)
        #Else If the Menu Choice is 3, call the exit_program function.
        elif menu_choice == "3":
            #Call the exit_program function.
            print("Exiting...")    
            break
        else:
            print("Invalid choice. Please select a valid option.")

#def movie_list():
def movie_list(movies):
    #Print the full movie list.
    print("Full Movie List:")
    for movie in movies:
        print(f"Title: {movie[0]} - Director: {movie[1]} -Genre: {movie[2]} "
              f"- Length: {movie[4]} min - Actors: {movie[5]}")

#def search for a movie
def search_movies(movies):
    #Ask user what they want to search by using choosing filters to apply (enter numbers separated by commas, e.g., 1,3):
    print("\nChoose which filters to apply (enter numbers separated by commas, e.g., 1,3):")
    #1. Genre
    print("1. Genre")
    #2. Director
    print("2. Director")
    #3. Actor
    print("3. Actor")
    #4. Length (min/max)
    print("4. Length (min/max)")
    #set search_by to an input asking the user to select filters and split the input by commas.
    search_by = input("Selected filters: ").split(",")
    #Initialize genre, director, actor, min_length, and max_length variables to None.
    genre = director = actor = None
    #Initialize min_length and max_length variables to None.
    min_length = max_length = None          
    #If "1" is in search_by, set genre to an input asking the user to enter a genre.
    if "1" in search_by:
        genre = input("Enter genre: ").lower()
    #If "2" is in search_by, set director to an input asking the user to enter a director.
    if "2" in search_by:
        director = input("Enter director: ").lower()
    #If "3" is in search_by, set actor to an input asking the user
    if "3" in search_by:
        actor = input("Enter actor: ").lower()
    #If "4" is in search_by, set min_length to an input asking the
    if "4" in search_by:
        min_length = input("Enter minimum length (minutes): ")
        max_length = input("Enter maximum length (minutes): ")
        #If min_length is not an empty string, convert it to an integer. If max_length is not an empty string, convert it to an integer.
        if min_length != "":
            min_length = int(min_length)
        if max_length != "":
            max_length = int(max_length)

    #Initialize results list to an empty list.
    results = []
    #for each movie in movies, unpack the movie into title, dir_name, genres, length, and actors. Convert length to an integer. Check if the movie matches the search criteria based on genre, director, actor, and length. If it matches, append the movie to the results list.
    for movie in movies:
        title, dir_name, genres, length, actors = movie
        length = int(length)
        #If genre is not None and genre is not in genres (case-insensitive), continue to the next movie.
        if genre and genre not in genres.lower():
            continue
        #If director is not None and director is not in dir_name (case-insensitive), continue to the next movie.
        if director and director not in dir_name.lower():
            continue
        #If actor is not None and actor is not in actors (case-insensitive), continue to the next movie.
        if actor and actor not in actors.lower():
            continue
        #If min_length is not None and length is less than min_length, continue to the next movie.
        if min_length is not None and length < min_length:
            continue
        #If max_length is not None and length is greater than max_length, continue to the next movie.
        if max_length is not None and length > max_length:
            continue
        #If all criteria are met, append the movie to results.
        results.append(movie)
    #Print the search results. If no movies are found, print a message indicating that no movies were found matching the criteria. Otherwise, print the title, genre, director, actors, and length of each movie in the results.
    print("\nSearch Results:")
    if len(results) == 0:
        print("No movies found matching the criteria.")
    else:
        for movie in results:
            print(f"Title: {movie[0]}, Genre: {movie[1]}, Director: {movie[2]}, Actors: {movie[3]}, Length: {movie[4]} minutes")

#Call the menu function with the loaded movies.
movies = load_movies()
menu(movies)