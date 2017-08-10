import turtle

def draw_flower():
    import turtle
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(40)
    for i in range(1, 180):
        brad.forward(100)
        brad.left(35)
        brad.forward(100)
        brad.left(145)
        brad.forward(100)
        brad.left(35)
        brad.forward(100)
        brad.right(2)

    brad.setheading(270)
    brad.forward(250)
    window.exitonclick()

draw_flower()

