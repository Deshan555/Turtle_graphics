import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

rainbow = turtle.Pen()

turtle.bgcolor('black')

for x in range(360):
    rainbow.pencolor(colors[x % 6])

    rainbow.width(x // 100 + 1)

    rainbow.forward(x)

    rainbow.left(59)
