import turtle
import colorgram
from turtle import Turtle, Screen
from random import choice

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 126)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)

turtle.colormode(255)

color_list = [(249, 248, 248), (237, 241, 245), (238, 246, 244), (249, 243, 247), (1, 12, 31), (53, 25, 17),
              (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24),
              (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
              (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85),
              (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178),
              (252, 197, 0), (29, 84, 92), (228, 174, 166), (186, 190, 201), (73, 73, 39)]

# tom = Turtle()
# screen = Screen()
# tom.speed(1)
# turtle.setworldcoordinates(-50, -50, 425, 425)
#
#
# def draw_hirst_painting():
#     for _ in range(100):
#         if _ == 10:
#             tom.goto(-10, -10)
#         tom.dot(20, choice(color_list))
#         tom.penup()
#         tom.forward(40)
#         tom.pendown()
#
#
# draw_hirst_painting()
# screen.exitonclick()

tim = Turtle()
screen = Screen()
screen.screensize(800, 1000)
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
