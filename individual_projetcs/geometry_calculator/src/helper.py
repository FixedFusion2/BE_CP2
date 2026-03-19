# TE 2nd Geometry Calculator
import math
import csv    

class Circle:
    def __init__(self, radius, name):
        self.name = name
        self.radius = radius

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

class Square:
    def __init__(self, base, height):
        self.base = base
        self.height = height

def circle_calc():
    name = input("Name your circle: ")
    radius = float(input("Enter the radius of your circle: "))
    area = math.pi*(radius**2)
    rounded_area = round(area, 2)
    perimeter = (radius*2)*math.pi
    rounded_perimeter = round(perimeter, 2)
    diameter = radius*2
    content = f"\nShape = Circle\nCircle Name = {name}\nCircle Radius = {radius} units\nArea = {rounded_area} units squared\nPerimeter = {rounded_perimeter} units\nDiameter = {diameter} units\n"
    print(content)
    with open("individual_projetcs\\geometry_calculator\\docs\\shapes.csv", "a") as file:
        file.write(content)


def triangle_calc():
    name = input("Name your triangle: ")
    base = float(input("Enter the base of your tiangle: "))
    height = float(input("Enter the height of your triangle: "))
    area = (base*height)/2
    content = f"\nShape = Triangle\nTriangle Name = {name}\nArea = {area} units squared\n"
    with open("individual_projetcs\\geometry_calculator\docs\\shapes.csv", "a") as file:
        file.write(content)
    
def rectangle_calc():
    name = input("Name your rectangle: ")
    base = float(input("Enter the base of your rectangle: "))
    height = float(input("Enter the height of your rectangle: "))
    area = (base*height)
    perimeter = (base*2) + (height*2)
    content = f"\nShape = Rectangle\nRectangle Name = {name}\nArea = {area} units squared\nPerimeter = {perimeter} units\n"
    with open("individual_projetcs\\geometry_calculator\\docs\\shapes.csv", "a") as file:
        file.write(content)

def square_calc():
    name = input("Name your square: ")
    base = float(input("Enter the base of your square: "))
    height = float(input("Enter the height of your square: "))
    area = (base*height)
    perimeter = (base*2) + (height*2)
    content = f"\nShape = Square\nSquare Name = {name}\nArea = {area} units squared\nPerimeter = {perimeter} units\n"
    with open("individual_projetcs\\geometry_calculator\\docs\\shapes.csv", "a") as file:
        file.write(content)

def view_shapes():
    print("📊 SHAPE LIBRARY:")
    with open("individual_projetcs\\geometry_calculator\\docs\\shapes.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def menu():
    while True:    
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

        choice = input("Choose your option (1-7): ")

        if choice == "1":
            print("1. Circle\n2. Triangle\n3. Rectangle\n4. Square")
            shape = input("Choose your option (1-4): ")
            if shape == "1":
                circle_calc()
            elif shape == "2":
                triangle_calc()
            elif shape == "3":
                rectangle_calc()
            elif shape == "4":
                square_calc()
            else:
                print("That is not an option.")
        elif choice == "2":
            view_shapes()
        elif choice == "3":
            print('Select a shape. ("finish this part.)')
        elif choice == "7":
            print("Exiting...")
            break
menu()