import csv
"""#To open a file in your program you have to use the open() function
with open("reading.txt", "r") as file:
    #Every time you refer to reading.txt it will be read as a file object.
    content = file.read()
    print(content)
"""



#To read a file line by line
"""while True:
    try:
        with open("BE_CP2/notes/reading.txt", "r") as file:
            for line in file:
                print(line.strip())
    except:
        print("That file can't be found.")
    else:
        print("File read successfully.")
        break"""
try:
    with open("BE_CP2/notes/sample.csv",mode = "r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        rows = []
        for line in content:
            rows.append(f"{headers[0]}: {line[0]}, {headers[1]}: {line[1]}")
except:
    print("That file can't be found.")
else:
    print("File read successfully.")