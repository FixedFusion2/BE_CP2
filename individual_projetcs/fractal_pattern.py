#TE 2nd Fractal Pattern Generator
import turtle


#Set the fill color
background_color = input("Type the background color you want: ")
triangle_color = input("Type the color you want the triangle: ")
turtle.setup(width=2000, height=1000)
screen = turtle.Screen()
t = turtle.Turtle()
#Begin filling
screen.bgcolor(background_color)
t.color(triangle_color)
#Use a loop to draw 3 sides
for i in range(3):
    t.forward(500)
    t.left(120)
for i in range(3):
    t.forward(250)
    t.left(120)
for i in range(3):
    t.forward(125)
    t.left(120)
for i in range(3):
    t.forward(62.5)
    t.left(120)
#End filling
turtle.done()

