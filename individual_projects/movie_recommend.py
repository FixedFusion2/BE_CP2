#TE 2nd Movie Recommender
#Import CSV
import csv
#Load in CSV file into list.
#Open the movies.csv file
def load_movies():
    movies = []
    try:
        with open("individual_projetcs/movies.csv", "r", encoding="utf-8") as csvfile:
            #Reader is set to csv.reader(csvfile)
            reader = csv.reader(csvfile)
            #For each row in the reader, append the row to the movies list.
            next(reader)
            for row in reader:
                if len(row) >= 6:
                    movies.append(row)
    except FileNotFoundError:
        print("Error: movies.csv file not found.")
    return movies
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
    if not movies:
        print("No Movies Loaded")
        return
    #Print the full movie list.
    print("\nFull Movie List:")
    print("-" * 80)
    #For movie in movies try and except and print title, director, genre, rating, length, actors.
    for movie in movies:
        try:
            title = movie[0]
            director = movie[1]
            genre = movie[2]
            rating = movie[3]
            length = movie[4]
            actors = movie[5]

            print(f"Title: {title}")
            print(f"Director: {director}")
            print(f" Genre: {genre}")
            print(f"Rating: {rating}")
            print(f"Length: {length} min")
            print(f"Actors: {actors}")
            print("-" * 80)
        except (IndexError, ValueError):
            print(f"Skipping malformed row: {movie}")
#def search for a movie
def search_movies(movies):
    if not movies:
        print("No movies loaded yet.")
        return
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
    search_by = input("Selected filters: ").strip()
    if not search_by:
        print("No filters selected, showing nothing.")
        return
    
    selected = [x.strip() for x in search_by.split(",")]
    #Initialize genre, director, actor, min_length, and max_length variables to None.
    genre = director = actor = None
    #Initialize min_length and max_length variables to None.
    min_length = max_length = None          
    #If "1" is in search_by, set genre to an input asking the user to enter a genre.
    if "1" in selected:
        genre = input("Enter genre: ").strip().lower()
    #If "2" is in search_by, set director to an input asking the user to enter a director.
    if "2" in selected:
        director = input("Enter director: ").strip().lower()
    #If "3" is in search_by, set actor to an input asking the user
    if "3" in selected:
        actor = input("Enter actor: ").strip().lower()
    #If "4" is in search_by, set min_length to an input asking the
    if "4" in selected:
        min_length = input("Enter minimum length (minutes) [press Enter to skip]: ").strip()
        max_length = input("Enter maximum length (minutes) [press Enter to skip]: ").strip()

    #Initialize results list to an empty list.
    results = []
    #for each movie in movies, unpack the movie into title, dir_name, genres, length, and actors. Convert length to an integer. Check if the movie matches the search criteria based on genre, director, actor, and length. If it matches, append the movie to the results list.
    for movie in movies:
        try:
            title = movie[0]
            dir_name = movie[1]
            gen_text = movie[2]
            length = int(movie[4].strip())
            actors = movie[5]

            match = True

            #If genre is not None and genre is not in genres (case-insensitive), continue to the next movie.
            if genre and genre not in gen_text.lower():
                match = False
            #If director is not None and director is not in dir_name (case-insensitive), continue to the next movie.
            if director and director not in dir_name.lower():
                match = False
            #If actor is not None and actor is not in actors (case-insensitive), continue to the next movie.
            if actor and actor not in actors.lower():
                match = False
            #If min_length is not None and length is less than min_length, continue to the next movie.
            if min_length is not None and length < min_length:
                match =False
            #If max_length is not None and length is greater than max_length, continue to the next movie.
            if max_length is not None and length > max_length:
                match = False
            if match:
            #If all criteria are met, append the movie to results.
                results.append(movie)
        except(IndexError, ValueError):
            continue
    #Print the search results. If no movies are found, print a message indicating that no movies were found matching the criteria. Otherwise, print the title, genre, director, actors, and length of each movie in the results.
    print("\nSearch Results:")
    if not results:
        print("No movies found matching the criteria.")
    else:
        for movie in results:
            try:
                print(f"Title: {movie[0]}")
                print(f"Genre: {movie[2]}")
                print(f"Director: {movie[1]}")
                print(f"Actors: {movie[5]}")
                print(f"Length: {movie[4]} minutes")
                print("-" * 60)
            except IndexError:
                continue
#Call the menu function with the loaded movies.
movies = load_movies()
menu(movies)