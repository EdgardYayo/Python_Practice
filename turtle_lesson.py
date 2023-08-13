import random
from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
turtle.shape("circle")

# DRAWING A SQUARE
# for i in range(0, 4):
#     turtle.forward(90)
#     turtle.right(90)

# DRAWING A DASHED LINE
# for i in range(0, 9):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()


# DRAWING SEVERAL SHAPES
# def draw_shapes(sides):
#     angle = 360 / sides
#     random_color = (
#             randint(0, 255),
#             randint(0, 255),
#             randint(0, 255)
#         )
#     hex = "#%02x%02x%02x" % random_color
#     for _ in range(sides):
#         turtle.forward(100)
#         turtle.color(hex)
#         turtle.right(angle)
#
#
# for sides in range(3, 11):
#     draw_shapes(sides)


# DRAWING A RANDOM WALK
def random_walking(step_size):
    directions = [0, 90, 180, 270]
    angle = random.choice(directions)
    random_pensize = random.randint(0, 25)
    turtle.forward(step_size)
    turtle.pensize(random_pensize)
    turtle.setheading(angle)

def random_color():
    random_color = (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )
    hex = "#%02x%02x%02x" % random_color
    turtle.color(hex)

for num in range(1000):
    turtle.speed("fastest")
    turtle.shape("turtle")
    random_color()
    random_walking(20)








screen = Screen()
screen.exitonclick()