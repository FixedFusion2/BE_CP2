# To read and write on a file use +.
"""with open("notes\\reading.txt", "r+") as file:
    content = file.read()
    content += "\nI wrote on my gilr"
    file.write(content)
 """
#with open("notes\\reading.txt", 'a') as file:
 #   file.write("\nThis is more on my file!")

#a means appends and w means write.
import csv

with open("notes\\sample.csv", 'r+', newline = '') as csvfile:
    fieldnames = ['username', 'color']
    reader = csv.reader(csvfile)
    for line in reader:
        print(f"{fieldnames[0]}, {line[0]} favorite color {line[1]}")
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerow({'username': 'aUser', 'color': 'pink'})
    writer.writerow({'username': 'mE', 'color': 'red'})
    writer.writerow({'username': 'yOU', 'color': 'green'})
    writer.writerow({'username': 'sOMeone', 'color': 'blue'})
    writer.writerow({'username': 'aPerson', 'color': 'red'})
    writer.writerow({'username': 'aNotherPerson', 'color': 'purple'})
    writer.writerow({'username': 'aCoolguy', 'color': 'black'})
    

print("Code is done.")