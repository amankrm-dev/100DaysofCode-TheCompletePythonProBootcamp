import random
import turtle
from turtle import Turtle
tim=Turtle()
turtle.colormode(255)
def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
tim.shape("turtle")
# corners=3
# colors=["red","green","tomato","yellow","skyblue","pink","blue"]
directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
# def draw(corners,color_index):
#     for i in range(corners):
#         deg = 360 / corners
#         tim.pencolor(colors[color_index % len(colors)])
#         tim.forward(100)
#         tim.right(deg)
#     corners+=1
#
#
# for shape_sides in range(3,11):
#     draw(shape_sides,shape_sides-3)

for _ in range(200):
    # tim.color(random.choice(colors))
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(directions))
turtle.exitonclick()