import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(200,200)

polygon=turtle.Turtle()
sides=4
sidelenght=90
angle=360/sides

for i in range (sides):
    polygon.forward(sidelenght)
    polygon.right(angle)

turtle.done()