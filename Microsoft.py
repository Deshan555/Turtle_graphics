from turtle import *

# this list contains the colors

colors = ['#f5480f','#2aad21','#288cf7','#ffcc00']

# this list stores all four positions

pos = [(0, 0), (100, 0), (0, -100), (100, -100)]

for (x, y),colors in zip(pos, colors):  # this loop will visit each positions and the colors using zip()

    up()  # lifting pen right before going there

    goto(x, y)

    down()  # putting down again afterwards

    fillcolor(colors)

    begin_fill()

    for i in range(4):
        forward(90)

        right(90)

    end_fill()
