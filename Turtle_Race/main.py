
from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tim = Turtle(shape="turtle")
jane = Turtle(shape="turtle")
pete = Turtle(shape="turtle")
mia = Turtle(shape="turtle")
sky = Turtle(shape="turtle")
pea = Turtle(shape="turtle")

turtles = [tim, jane, pete, mia, sky, pea]


screen.setup(width=800, height=800)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

positions = [100, 50, 0, -50, -100, -150]

for turtle_i in range(0, 6):
    current_turtle = turtles[turtle_i]
    current_turtle.color(colors[turtle_i])
    current_turtle.penup()
    current_turtle.goto(x=-350, y=positions[turtle_i])


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 370:
            j = turtles.index(turtle)   # We need this variable to check out the index of the turtle winner that matches with its index name in the list turtles
            is_race_on = False

            if turtle.pencolor() == user_bet.lower():
                print(f"The {colors[j]} turtle won!! so you won!!")
            else:
                print(f"The {colors[j]} turtle won!! so you lose!!")
                

        turtle.forward(randint(0, 10))


screen.exitonclick()