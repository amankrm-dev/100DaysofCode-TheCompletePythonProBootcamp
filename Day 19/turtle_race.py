import random
from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which  turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]

start_x=-230
start_y=-100
spacing=50
turtles=[]

for i in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=start_x,y=start_y+ i*spacing)
    turtles.append(tim)

if user_bet:
    race_on=True
    while race_on:
        for turtle in turtles:
            distance=random.randint(0,10)
            turtle.forward(distance)

            if turtle.xcor()>230:
                race_on=False
                winning_color=turtle.pencolor()

                if winning_color==user_bet.lower():
                    print(f"You have won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You have lost! The {winning_color} turtle is the winner!")


screen.exitonclick()