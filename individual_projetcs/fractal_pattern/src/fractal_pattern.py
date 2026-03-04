#TE 2nd Fractal Pattern Generator

#OVERVIEW:
#Create a Python program that generates a Sierpinski Triangle fractal pattern using recursion. The program should allow users to customize the recursion depth and color of the fractal.

#PROJECT STEPS:
#Implement a main function that runs the program and handles user input
#Create a function to draw the Sierpinski Triangle using recursion
#Use Python's turtle graphics module for drawing
#Allow users to specify:
#Recursion depth (1-5)
#Triangle color
#HINT: Remember to implement a base case in your recursive function to prevent infinite recursion!
#HINT: Use thins image to help you think about HOW to draw this with turtle!
import turtle

#Def Fractal Triangle()
def draw_triangle(t,size, color):
    #Set color and begin filling the background
    t.fillcolor(color)
    t.begin_fill()
    #Draw Triangle
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Recursive Sierpinski Triangle function
def sierpinski(t, size, depth, color):
    #Base Case
    if depth == 0:
        draw_triangle(t, size, color)
    else:
        #Bottom Left
        sierpinski(t,size/2,depth-1,color)
        #Bottom Right
        t.forward(size/2)
        sierpinski(t,size/2,depth-1,color)
        #Top
        t.backward(size/2)
        t.left(60)
        t.forward(size/2)
        sierpinski(t,size/2,depth-1,color)
        t.backward(size/2)
        t.right(60)
        #Return to original position
        t.forward(60)
        t.backward(size/2)
        t.right(60)


def main():
    #Print  Welcome to the Sierpinski triangle generator. This program makes a fractal using recursion.
    print("Welcome to the Sierpinski triangle generator. This program makes a fractal using recursion.")
    #Depth is set to an input asking for the user to enter recursion depth 1-5, get depth as an integer.
    depth = int(input("Enter recursion depth(0-5): "))
    color = input("Enter triangle color: ")
    print('\nGenerating Sierpinski Triangle...')
    #Setup screen and turtle
    screen = turtle.Screen()
    screen.setup(1000,800)
    #t is set to a turtle
    t = turtle.Turtle()
    t.speed(0) # Set turtle speed to maximum
    t.penup()
    t.goto(-300, -250) # Move turtle to starting position
    t.pendown()

    sierpinski(t, 600, depth, color) # Draw Sierpinski Triangle with specified depth and color

    print('Fractal generation complete!')
    print('Click on the window to exit.')
    screen.exitonclick() # Wait for user to click before closing the window

#Run Main()
main()