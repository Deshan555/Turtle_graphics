from turtle import *  # import library

bgcolor('black')  # Background color set as Black

color('red', 'yellow')  # Color Fills

begin_fill()

while True:

    forward(200)

    left(170)

    if abs(pos()) < 1:
        break

end_fill()

done()
