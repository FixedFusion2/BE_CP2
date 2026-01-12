#TE 2nd Types of List Notes

siblings = ["Morgan", "Honor", "Joy"]#list
#list methods
siblings.append("NewSibling")#adds an item to the end of a list
siblings.insert(1,"InsertedSibling")#inserts an item at a specific index
siblings.clear()
siblings.extend(["Sibling1","Sibling2"])#adds multiple items to a list
siblings.copy()#creates a shallow copy of the list
siblings.remove("Joy")#removes a specific item from a list
siblings.pop()#removes the last item from a list
siblings.sort()#sorts the list in ascending order
#and there are a couple more methods
print(siblings)
print(siblings[2])
siblings[2] = "NewName"
print(siblings)

fruit = ("Apple", "Banana", "Cherry")#tuple
#tuple methods
fruit.count("Apple")#counts how many times an item appears in a tuple
fruit.index("Banana")#finds the index of an item in a tuple
#lists are changable where tuples are not
home = (0,0)#lists are helpful for permanent save data like coordinates
x,y = home
print(x)
print(y)

#set
colors = {"red", "green", "blue","orange"}#sets are surrounded by braces
colors.add("Pink")#can add items to a set
colors.remove("green")#can remove items from a se
print(colors)#sets are unordered collections of unique elements
#no duplicates in a set

for i in colors:
    if i == "orange":
        print("fruit")
    print(i)
#The purpose of a set is for membership testing and eliminating duplicate items.
#set methods
colors.clear()#removes all items from a set
colors.add("Yellow")#adds an item to a set
colors.pop()#removes and returns an arbitrary item from a set
#there are several more methods available for sets
