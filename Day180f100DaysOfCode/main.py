# import colorgram
# import turtle as t
#
# kago = t.Turtle()
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
# print(rgb_colors)
# Making a damien hirst painting
import turtle as t
import random

kago = t.Turtle()
kago.speed("fastest")
t.colormode(255)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

kago.up()
kago.setheading(225)
kago.forward(250)
kago.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots +1 ):
    kago.dot(20, random.choice(color_list))
    # kago.up()
    kago.forward(50)
    # kago.up()

    if dot_count % 10 == 0:
        kago.setheading(90)
        kago.forward(50)
        kago.setheading(180)
        kago.forward(500)
        kago.setheading(0)

kago.ht()


screen = t.Screen()
screen.exitonclick()
