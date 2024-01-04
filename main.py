from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()
my_screen = Screen()
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


for _ in range(500):
    angle = random.randrange(0, 360, 90)
    my_turtle.speed(9)
    my_turtle.pensize(10)
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(angle)

my_screen.exitonclick()
