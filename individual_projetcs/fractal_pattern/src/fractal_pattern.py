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

def main():
    #Print  Welcome to the Sierpinski triangle generator. This program makes a fractal using recursion.
    print("Welcome to the Sierpinski triangle generator. This program makes a fractal using recursion.")
    #Depth is set to an input asking for the user to enter recursion depth 1-5.
    depth = input("Enter recursion depth(1-5): ")
    #t is set to a turtle
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(2000,1000)
    #Print Generator triangle
    print('Generating Triangle...')
    #Run Triangle Generator(depth)
    fractal_triangle(t,screen,depth)


#Def Fractal Triangle()
def fractal_triangle(t,screen,depth):
    if depth == "1":
        #for loop that draws a triangle
        for i in range(3):
            #Forwward 500
            t.forward(500)
            #Turn Left 120
            t.left(120)
    if depth == "2":
        #for loop that draws a triangle
        for i in range(3):
            #Forwward 500
            t.forward(500)
            #Turn Left 120
            t.left(120)
        #Penup
        #Move location rleative to the side
        #Pendown
        for i in range(3):
            #Forwward 500
            t.forward(250)
            #Turn Left 120
            t.left(120)

        t.penup()
        t.setpos(250,0)
        t.pendown()
        for i in range(3):
            #Forwward 500
            t.forward(250)
            #Turn Left 120
            t.left(120)
        t.penup()
        t.setpos(0,0)
        t.pendown()
        t.left(60)
        t.forward(250)
        t.right(60)
        t.forward(250)
        screen.exitonclick()
    #For loop that makes the triangle half as small
    #Repeat this at the depth recursion is set to.
#Run Main()
main()