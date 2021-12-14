from turtle import *

width(20)

bgcolor('black')

colors = ['#db0f3c', '#50ebe7', 'white']

positions = [(0, 0), (-5, 13), (-5, 5)]  # Start Positions

for (x, y), col in zip(positions, colors):
    up()

    goto(x, y)

    down()

    color(col)

    left(180)

    circle(50, 270)

    forward(120)

    left(180)

    circle(50, 90)
