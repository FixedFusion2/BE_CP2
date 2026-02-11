import csv

library = []

book = input("Choose book: ")
author = input("Author to book: ")




with open("individual_projetcs\\library.csv", "a", newline = '') as csvfile:
    fieldnames = ['author','book']
    reader = csv.reader(csvfile)
    for line in reader:
        print(f"{fieldnames[0]}, {line[0]} book {line[1]}")
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerow({'author': author, "book": book})

    library.append({"Title": book, "Author": author})
    print("Library")