#TE 2nd Fractal Pattern Generator
import turtle

turtle.setup(width=2000, height=1000)

t = turtle.Turtle()
t.speed(10000000000000000000000000000000000000000000000000000000000000000)
screen = turtle.Screen()

t.color("blue")

for i in range(3):
    t.forward(300)
    t.left(120)
for i in range(3):
    t.forward(200)
    t.left(120)
for i in range(3):
    t.forward(100)
    t.left(120)
for i in range(3):
    t.forward(50)
    t.left(120)
for i in range(3):
    t.forward(25)
    t.left(120)
for i in range(3):
    t.forward(12.5)
    t.left(120)
for i in range(3):
    t.forward(6.25)
    t.left(120)



# Draw one filled triangle
def draw_triangle(t, size, color):
    # TODO:
    # 1. Set the fill color
    # 2. Begin filling
    # 3. Use a loop to draw 3 sides
    # 4. End filling
    
    pass


turtle.done()