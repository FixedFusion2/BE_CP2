import csv
import os
# Store the path to the CSV file used to save the library
file_path = "individual_projects/library.csv"
# Define the column that names every item in the libary will use
fieldnames = ["title", "creator", "year", "genre", "format", "rating", "notes"]

#Def load library
def load_library():
    #Create library list
    library = []
    #Check if the file does not exsist
    if not os.path.exists(file_path):
        #Open the file in write mode to create it
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        #Write the header row to the CSV file
        writer.writeheader()
    #Return an empty library since no data exsists yet
    return library

    #Open the exsisting CSV file
    with open(file_path, "r", newline="", encoding= "utf-8") as f:
        #create a dictreader to read rows as dictionaries
        reader =csv.DictReader(f)
        #Loop through each row in the CSV file
        for row in reader:
            #Try to add teh row to the library list
            try:
                library.append(row)
            #If a row is malformed, skip it
            except Exception:
                print("Skipped a bad row in the file.")

    #Return the loaded libary list
    return library

#Def save library
def save_library(library):
    #Open the CSV file in the write mode (overwrites file)
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        #Create a dictwriterusing the required fieldnames
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        #Write the hbeader row
        writer.writeheader()
        #Write every dictionary in the library list
        writer.writerows(library)
    #Tell the user the library was saved
    print("Library saved.")

#Def show simple
def show_simple(library):
    #Check if the library is empty:
    if not library:
        print("Library is empty.")
        return
    #Loop through each item and its index
    for i, item in enumerate(library, start=1):
        #Print the item number, title, and creator
        print(f"{i}. {item['title']} - {item['creator']}")

#Def show detailed
def show_detailed(library):
    #Check if the library is empty
    if not library:
        print("Library is empty.")
        return
    #Loop through each item and its index
    for i, item in enumerate(library, start=1):
        #Print the item number
        print(f"\nItem {i}")
        #Loop through every fieldname
        for key in fieldnames:
            #Print the field name and its value
            print(f"{key.title()}: {item.get(key, '')}")

#Crud Functions

#Def add item
def add_item(library):
    #Create an empty dictionary for the new item
    item = {}

    #Ask user for the title
    item["title"] = input("Title: ").strip()
    #Ask user for the creator
    item["creator"] = input("Creator (author/artist/director): ").strip()
    #Ask user for the year
    item["year"] = input("Year: ").strip()
    #Ask user for the genre
    item["genre"] = input("Genre: ").strip()
    #Ask user for the format
    item["format"] = input("Format: ").strip()
    #Ask user for the rating
    item["rating"] = input("Rating: ").strip()
    #Ask user for notes
    item["notes"] = input("Notes: ").strip()

    #Add the new item dictionary to the library list
    library.append(item)
    #Tell the user the item was added
    print("Item added.")
    #Return True to indicate unsaved changes
    return True

#Def update item
def update_item(library):
    #Show the simple list so the user can choose
    show_simple(library)
    #Try to get the item number from the user
    try:
        #Convert user input to an index
        index = int(input("Enter item number to update: ")) - 1
        #Access the selected item
        item = library[index]
    #handle invalid input or index
    except (ValueError, IndexError):
        print("Invalid Selection")
        return False
    #loop through every field
    for key in fieldnames:
        #Ask for a new value, showing the old value
        new_value = input(f"{key.title()} ({item[key]}): ").strip()
        #Update only if the user typed something
        if new_value:
            item[key] = new_value
    #Tell the user the item was updated
    print("Item Updated")
    #Return True to indicate unsaved changes
    return True


#Def Delete item
def delete_item(library):
    #Show the simple list so the user can choose
    show_simple(library)
    #Try to get the item number for the user
    try:
        #Convert user input to an index
        index = int(input("Enter item number to delete: ")) - 1
        #Remove the selected item
        removed = library.pop(index)
        #Confirm deletion to the user
        print(f"Deleted '{removed['title']}'.")
        #Return True to indicate unsaved changes
        return True
    #Handle invalid input or index
    except (ValueError, IndexError):
        print("Invalid Selection.")
        return False

#Def Main
def main():
    #load the library from the CSV file
    library = load_library()

    #track whether there are unsaved changes
    unsaved_changes = False

    #Run the program until the user chooses to exit
    while True:
        #Display the main menu
        print("\n---Personal Library---")
        print("1. Show Simple List")
        print("2. Show Detailed List")
        print("3. Add Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Save Library")
        print("7. Reload Library From File")
        print("8. Exit")

        #Ask user for their menu choice
        choice = input("Choose an option: ").strip()

        #If the User wants a simple list
        if choice == "1":
            show_simple(library)
        #If the User wants a detailed list
        if choice == "2":
            show_detailed(library)
        #If the User wants to add an item
        if choice == "3":
            unsaved_changes |= add_item(library)
        #If the User wants to update an item
        if choice == "4":
            unsaved_changes |= update_item(library)
        #If the User wants to delete an item
        if choice == "5":
            unsaved_changes |= delete_item(library)
        #If the User wants to save
        elif choice == "6":
            save_library(library)
            unsaved_changes = False
        #If the User wants to reload from file
        elif choice == "7":
            library = load_library()
            unsaved_changes = False
            print("Library Reloaded")
        #If the User wants to exit
        elif choice == "8":
            #Check for unsaved changes
            if unsaved_changes:
                #Ask whether to save before exiting
                save = input("You have unsaved changes. Save? (y/n): ").lower()
                #Save if the user says yes
                if save == "y":
                    save_library(library)
            #Exit program loop
            print("Exiting...")
            break
        #Handle invalid menu choices
        else:
            print("Invalid option. Try Again.")

#Call Main Function
main()