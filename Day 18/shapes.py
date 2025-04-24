import turtle
from turtle import Turtle
tim=Turtle()
tim.shape("turtle")
# corners=3
colors=["red","green","tomato","yellow","skyblue","pink","blue"]

def draw(corners,color_index):
    for i in range(corners):
        deg = 360 / corners
        tim.pencolor(colors[color_index % len(colors)])
        tim.forward(100)
        tim.right(deg)
    corners+=1


for shape_sides in range(3,11):
    draw(shape_sides,shape_sides-3)



turtle.exitonclick()