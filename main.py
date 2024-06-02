from turtle import Turtle, Screen, colormode
import random

color_list = [(172, 43, 53), (218, 213, 124), (104, 155, 117), (240, 246, 243), (103, 169, 225), (128, 18, 34),
              (199, 153, 75), (173, 142, 188), (3, 153, 171), (44, 42, 40), (1, 52, 91), (121, 119, 160),
              (239, 242, 247), (77, 176, 97)]

pointer = Turtle()
pointer.speed("fastest")
colors_mode = colormode(255)
pointer.hideturtle()
pointer.penup()
pointer.setpos(-250, -250)
x = -250

for _ in range(10):
    for _ in range(10):
        random_color = random.choice(color_list)
        pointer.dot(20, random_color)
        pointer.forward(50)
    x += 50
    pointer.setpos(-250, x)


screen = Screen()
screen.exitonclick()
print(screen)