# TE 2nd Geometry Calculator
import math
    
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
    print(f"Your Circle {name} has a Radius of {radius} units, an Area of {rounded_area} units squared, a perimeter of {rounded_perimeter} units, and a diameter of {diameter} units.")

def triangle_calc():
    name = input("Name your triangle: ")
    base = float(input("Enter the base of your tiangle: "))
    height = float(input("Enter the height of your triangle: "))
    area = (base*height)/2
    print(f"Your Triangle, {name}, has an area of {area} units squared.")
    
def rectangle_calc():
    name = input("Name your rectangle: ")
    base = float(input("Enter the base of your rectangle: "))
    height = float(input("Enter the height of your rectangle: "))
    area = (base*height)
    perimeter = (base*2) + (height*2)
    print(f"Your Rectangle, {name}, has an area of {area} units squared, and a perimeter of {perimeter} units.")

def square_calc():
    name = input("Name your square: ")
    base = float(input("Enter the base of your square: "))
    height = float(input("Enter the height of your square: "))
    area = (base*height)
    perimeter = (base*2) + (height*2)
    print(f"Your square, {name}, has an area of {area} units squared, and a perimeter of {perimeter} units.")

