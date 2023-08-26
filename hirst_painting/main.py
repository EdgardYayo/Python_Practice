# import colorgram
from turtle import Turtle, Screen
import turtle
import random

# EXTRACTING THE COLORS OF A IMAGE
# rgb_colors = []
# colors = colorgram.extract('/Users/allan/Desktop/Desktop files/phyton projects/Python Basics Practice/hirst_painting/spots_art.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# print(rgb_colors)

color_list = [(13, 34, 51), (216, 209, 214), (41, 114, 140), (222, 172, 8), (54, 13, 22), (143, 165, 182), (198, 171, 106), (48, 136, 15), (140, 56, 100), (17, 31, 128), (220, 207, 108), (65, 125, 204), (188, 98, 26), (229, 205, 7), (133, 24, 49), (146, 10, 6), (183, 154, 166), (147, 180, 134), (30, 117, 3), (88, 161, 53), (50, 15, 13), (181, 189, 208), (59, 153, 175), (16, 26, 24), (178, 207, 164), (171, 101, 119), (16, 83, 103)]

tim = Turtle()
tim.shape('turtle')
turtle.colormode(255)

tim.speed("fastest")
tim.setheading(200)
tim.penup()
tim.forward(380)
tim.setheading(0)

def spot_artist():
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

for _ in range(0, 10):
    for _ in range(0, 11):
        spot_artist()

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(550)
    tim.setheading(0)

tim.hideturtle()


screen = Screen()
screen.exitonclick()