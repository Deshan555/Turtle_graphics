from turtle import *  # import turtle library

width(20)

bgcolor('black')  # add background color

colors = ['#db0f3c', '#50ebe7', 'white']  # That list contain all colors

positions = [(0, 0), (-5, 13), (-5, 5)]  # Start Positions

for (x, y), col in zip(positions, colors):  # using zip() to combine color with position
    up()

    goto(x, y)

    down()

    color(col)

    left(180)

    circle(50, 270)

    forward(120)

    left(180)

    circle(50, 90)
