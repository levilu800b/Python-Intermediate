# Generate a random walk

import turtle as t
import random


timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")

for _ in range(1000):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()