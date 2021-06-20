import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
turtle.colormode(255)
# rgb_colors = []
# colors = colorgram.extract("hirst_painting.jpg",30)
#
# for color in colors :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color= (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

# painting = []
#
# for i in range(20):
#     liste = []
#     for j in range(3):
#         a = random.randint(0,255)
#         liste.append(a)
#     painting.append(tuple(liste))
# print(painting)
tim.penup()
tim.hideturtle()
tim.goto(-300,-300)
tim.pendown()
x = -300
y = -300
for i in range(10):
    tim.dot(20, *random.choices(color_list))
    tim.penup()
    tim.forward(60)
    tim.pendown()
    for i in range(10):
        tim.penup()
        tim.dot(20, *random.choices(color_list))
        tim.forward(60)
    y += 60
    tim.goto(x,y)





screen = Screen()
screen.exitonclick()