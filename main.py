# import colorgram as c
# my_color = c.extract('image.jpg', 30)
#
# init_col = []
#
# for color in my_color:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     init_col.append(new_color)
# print(init_col)

from turtle import Turtle, Screen, colormode
import random

tom = Turtle()
tom.pu()
colormode(255)

m_screen = Screen()
m_color_list = [(244, 228, 79), (162, 75, 42), (216, 146, 90), (23, 30, 61), (124, 160, 218), (54, 89, 145), (45, 36, 30), (40, 48, 114), (29, 44, 34), (147, 56, 81), (131, 31, 43), (203, 82, 120), (146, 31, 25), (214, 80, 55), (69, 31, 41), (67, 113, 77), (133, 182, 164), (94, 105, 200), (193, 140, 155), (72, 79, 40), (96, 162, 82), (153, 207, 220), (156, 186, 235), (48, 87, 32), (171, 165, 69), (229, 169, 185)]

tom.speed(0)
no_steps = 100
tom.setheading(225)
tom.forward(300)
tom.setheading(0)


def next_draw():
    # x position become 300 cos 45
    tom.setpos(-212.13, tom.pos()[1]+50)


while no_steps > 0:
    for _ in range(10):
        tom.dot(15, random.choice(m_color_list))
        tom.forward(50)
        no_steps -= 1

    next_draw()
    tom.hideturtle()

m_screen.exitonclick()
