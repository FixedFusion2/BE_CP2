# TE 2nd Geometry Calculator
#Importing necessary libraries
import math
import csv
#Importing the os library to check the operating system and clear the console accordingly
from os import name    

#Creating classes for each shape
#Circle class with methods to calculate area and perimeter
class Circle:
    def __init__(self, radius, name):
        self.name = name
        self.radius = radius
    def area(self):
        return round(math.pi * self.radius**2,2)
    
    def perimeter(self):
        return round(2 * math.pi * self.radius,2)
    def display(self):
        print(f"\nShape = Circle")
        print(f"Name = {self.name}")
        print(f"Radius = {self.radius} units")
        print(f"Area = {self.area()} units squared")
        print(f"Perimeter = {self.perimeter()} units")
        print(f"Diameter = {self.radius*2} units\n")

        content = f"\nShape = Circle\nName = {self.name}\nRadius = {self.radius} units\nArea = {self.area()} units squared\nPerimeter = {self.perimeter()}\nDiameter = {self.radius*2} units\n"
        with open("individual_projetcs\\geometry_calculator\\docs\\shapes.csv", "a") as file:
            file.write(content)
    #Static method to display formulas for circle calculations
    @staticmethod
    #This method is static because it does not depend on any instance of the Circle class. It simply prints out the formulas for calculating the area, perimeter, and diameter of a circle.
    def formula():
        #Formulas for calculating area, perimeter, and diameter of a circle
        print("Circle: Area = π * r^2 | Perimeter = 2 * π * r | Diameter = 2 * r")
#Triangle class with methods to calculate area
class Triangle:
    def __init__(self, base, height,name):
        self.name = name
        self.base = base
        self.height = height
    def area(self):
        return round((self.base * self.height) / 2, 2)
    def display(self):
        print(f"\nShape = Triangle")
        print(f"Name = {self.name}")
        print(f"Base = {self.base} units")
        print(f"Height = {self.height} units")
        print(f"Area = {self.area()} units squared\n")

        content = f"\nShape = Triangle\nName = {self.name}\nBase = {self.base} units\nHeight = {self.height} units\nArea = {self.area()}\n"
        with open("individual_projetcs\\geometry_calculator\\docs\\shapes.csv", "a") as file:
            file.write(content)
    #Static method to display formulas for triangle calculations
    @staticmethod
    def formula():
        #Formula for calculating area of a triangle
        print("Triangle: Area = (base * height) / 2")
#Rectangle class with methods to calculate area and perimeter        
class Rectangle:
    def __init__(self, base, height,name):
        self.base = base
        self.height = height
        self.name = name

    def area(self):
        return round(self.base * self.height, 2)
    def perimeter(self):
        return round(2 * (self.base + self.height), 2)
    def display(self):
        print(f"\nShape = Rectangle")
        print(f"Name = {self.name}")
        print(f"Base = {self.base} units")
        print(f"Height = {self.height} units")
        print(f"Area = {self.area()} units squared")
        print(f"Perimeter = {self.perimeter()} units\n")

        content = f"\nShape = Rectangle\nName = {self.name}\nBase = {self.base} units\nHeight = {self.height} units\nArea = {self.area()}\nPerimeter = {self.perimeter()} units\n"
        with open("individual_projetcs\\geometry_calculator\\docs\\shapes.csv", "a") as file:
            file.write(content)
    #Static method to display formulas for rectangle calculations
    @staticmethod
    def formula():
        #Formulas for calculating area and perimeter of a rectangle
        print("Rectangle: Area = base * height | Perimeter = 2 * (base + height)")
        

class Square:
    def __init__(self, base, height,name):
        self.base = base
        self.height = height
        self.name = name
    def area(self):
        return round(self.base * self.height, 2)
    def perimeter(self):
        return round(2 * (self.base + self.height), 2)
    def display(self):
        print(f"\nShape = Square")
        print(f"Name = {self.name}")
        print(f"Base = {self.base} units")
        print(f"Height = {self.height} units")
        print(f"Area = {self.area()} units squared")
        print(f"Perimeter = {self.perimeter()} units\n")
        
        content = f"\nShape = Rectangle\nName = {self.name}\nBase = {self.base} units\nHeight = {self.height} units\nArea = {self.area()}\nPerimeter = {self.perimeter()} units\n"
        with open("individual_projetcs\\geometry_calculator\\docs\\shapes.csv", "a") as file:
            file.write(content)
    #Static method to display formulas for square calculations
    @staticmethod
    def formula():
        #Formulas for calculating area and perimeter of a square
        print("Square: Area = base * height | Perimeter = 2 * (base + height)")
#Global Shape list
shapes = []
#Functions for each shape calculation and menu display
#Circle Calculation.
def circle_calc():
    #tTry and except to handle invalid input.
    try:
        #Name and radius input for the circle. The radius must be a positive number.
        name = input("Name your circle: ")
        radius = float(input("Enter radius (postive number): "))
        if radius <= 0:
            print("Error: Must be positive.")
            return
        c = Circle(radius,name)
        shapes.append(c)
        c.display()
    except:
        print("Error: Invalid input.")

#Triangle Calculation.
def triangle_calc():
    #Try and except to handle invalid input.
    try:
        #Name, base, and height input for the triangle. The base and height must be positive numbers.
        name = input("Name your triangle: ")
        base = float(input("Enter the base of your triangle: "))
        height = float(input("Enter the height of your triangle: "))
        if base <= 0 or height <= 0:
            print("Error: Must be positive.")
            return
        t = Triangle(base,height)
        shapes.append(t)
        t.display()
    except:
        print("Error: Invalid input.")

#Rectangle Calculation.    
def rectangle_calc():
    #Try and except to handle invalid input.
    try:
        #Name, base, and height input for the rectangle. The base and height must be positive numbers.
        name = input("Name your rectangle: ")
        base = float(input("Enter the base of your rectangle: "))
        height = float(input("Enter the height of your rectangle: "))
        if base <= 0 or height <= 0:
            print("Error: Must be positive.")
            return
        r = Rectangle(base,height)
        shapes.append(r)
        r.display()
    except:
        print("Error: Invalid input.")

#Square Calculation.        
def square_calc():
    try:
        #Name, base, and height input for the square. The base and height must be positive numbers.
        name = input("Name your square: ")
        base = float(input("Enter the base of your square: "))
        height = float(input("Enter the height of your square: "))
        if base <= 0 or height <= 0:
            print("Error: Must be positive.")
            return
        s = Square(base,height)
        shapes.append(s)
        s.display()
    except:
        print("Error: Invalid input.")

#Functions for view, compare, and sort.
#View Shapes function.
def view_shapes():
    #If not shapes in the shapes list, print a message and return. Otherwise, loop through the shapes list and display each shape's name and details.
    if not shapes:
        print("No shapes yet, create a shape first.")
        return
    for i, shape in enumerate(shapes):
        print(f"[{i}] {shape.name}")
#Compare Function.
def compare_shapes():
    #If the length of shapes is less than 2, print a message and return.
    if len(shapes) < 2:
        print("Need at least 2 shapes to compare.")
        return
    #Try and except to handle invalid input.
    try:
        #Call the view_shapes function.
        view_shapes()
        i1 = int(input("Select the first shape to compare (index): "))
        i2 = int(input("Select the second shape to compare (index): "))
        s1 = shapes[i1]
        s2 = shapes[i2]

        if s1.area() > s2.area():
            print(f"{s1.name} has a larger area.")
        else:
            print(f"{s2.name} has a larger area.")

        #Compare perimeters if both shapes have a perimeter.
        #If both shapes have a perimeter method, compare their perimeters and print which one is larger. 
        #If either shape does not have a perimeter method, skip this comparison.
        if hasattr(s1, 'perimeter') and hasattr(s2, 'perimeter'):
            if s1.perimeter() > s2.perimeter():
                print(f"{s1.name} has a larger perimeter.")
            else:
                print(f"{s2.name} has a larger perimeter.")
    except:
        print("Error: Invalid input.")

#Sort Shapes Function.
def sort_shapes():
    #Key is set to an input asking if they want area or perimeter.
    key = input("Sort by area or perimeter? (a/p): ")
    if key == "a":
    #Lamda is used to sort the shapes list based on the area of each shape.
        sorted_shapes = sorted(shapes, key=lambda s: s.area())
    elif key == "p":
    #hasattr is used to check if each shape has a perimeter method.
        sorted_shapes = sorted(shapes, key=lambda s: s.perimeter() if hasattr(s, 'perimeter') else 0)
    else:
        print("That is not an option.")
        return
    #Loop through the sorted shapes and display each shape's name and details.
    print("Sorted Shapes:")
    for s in shapes:
        s.display()

#Formula Guide Function.
def formula_guide():
    #Use Classes to call the static formula method for each shape.
    Circle.formula()
    Triangle.formula()
    Rectangle.formula()
    Square.formula()

#Menu System.
#Menu Function.
def menu():
    #While loop, stops when user exits.
    while True:
        #Print Menu options.    
        print("=====================================")
        print("📐 GEOMETRY CALCULATOR 📐")
        print("=====================================")
        print("Current Shapes: 0 created")
        print("🎯 ACTIONS:")
        print("[1] Create New Shape")
        print("[2] View All Shapes")
        print("[3] Select Shape")
        print("[4] Compare Shapes")
        print("[5] Sort Shapes")
        print("[6] Formula Guide")
        print("[7] Quit")

        #Choice for user input
        choice = input("Choose your option (1-7): ")

        #If choice is set to 1 create a new shape.
        if choice == "1":
            print("\n[1] Circle ⭕\n[2] Rectangle 📋\n[3] Square\⬜\n[4] Triangle 🔺\n")
            shape_choice = input("Choose your option (1-4): ")
            if shape_choice == "1":
                circle_calc()
            elif shape_choice == "2":
                rectangle_calc()
            elif shape_choice == "3":
                square_calc()
            elif shape_choice == "4":
                triangle_calc()
            else:
                print("Invalid option.")
        #If choice is set to 2 view all shapes.
        elif choice == "2":
            view_shapes()
        #If choice is set to 3 select a shape and view its details.
        elif choice == "3":
            view_shapes()
            try:
                idx = int(input("Select shape index: "))
                shapes[idx].display()
            except:
                print("Invalid selection.")
        #If choice is set to 4 compare two shapes.
        elif choice == "4":
            compare_shapes()
        #If choice is set to 5 sort shapes by area or perimeter.
        elif choice == "5":
            sort_shapes()
        #If choice is set to 6 display the formula guide.
        elif choice == "6":
            formula_guide()
        #If choice is set to 7 exit the program.
        elif choice == "7":
            print("Exiting...")
            break
        #Else statement for invalid menu options.
        else:
            print("Invalid option. Please choose a number between 1 and 7.")

#Run the menu function to start the program.
menu()