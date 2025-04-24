# import turtle
from turtle import Turtle, Screen

tim=Turtle()
tim.shape("turtle")
tim.color("tomato")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
#
# import turtle as t
# tom=t.Turtle()
# tim.shape("turtle")
# tim.color("green")
#
# import heroes
# print(heroes.gen())



for _ in range(15):
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.forward(10)

screen=Screen()
screen.exitonclick()