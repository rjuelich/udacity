import turtle
import math


def draw_fractal():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(20)
    brad.color("green")
    s = 0
    while s <= 180:
        n = 0
        while n < 4:
            brad.forward(100)
            brad.right(90)
            n += 1

        brad.penup()
        brad.forward(2)
        brad.left(90)
        brad.forward(2)
        brad.right(145)
        brad.pendown()
        s += 1

    window.exitonclick()


draw_fractal()






