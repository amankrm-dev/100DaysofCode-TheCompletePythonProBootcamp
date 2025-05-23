import random
import turtle as t
tim=t.Turtle()
t.colormode(255)
def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
tim.speed("fastest")
def draw_spirograph(size_of_graph):
    for _ in range(int(360/size_of_graph)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_graph)

draw_spirograph(5)
screen=t.Screen()
screen.exitonclick()