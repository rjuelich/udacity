import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    n=0
    while n < 4:
        brad.forward(100)
        brad.right(90)
        n += 1

def draw_circle():
    #window = turtle.Screen()
    #window.bgcolor("red")
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


def draw_triangle():
    #window = turtle.Screen()
    #window.bgcolor("red")
    blah = turtle.Turtle()
    blah.shape("turtle")
    blah.color("purple")
    n=0
    while n < 3:
        blah.forward(100)
        blah.right(120)
        n += 1


draw_square()
draw_circle()
draw_triangle()

window.exitonclick()
