import turtle

angle1 = [180, 135, 90, 45, 0]


def star(color, sides, length, angle,
         distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colourful!
    galileo.width(5)  # visible!
    galileo.speed(8)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
        galileo.hideturtle()  # just the star


star("gold", 5, 50, 0, 100)
star("green", 5, 50, 45, 100)
star("red", 5, 50, 90, 100)
star("blue", 5, 50, 135, 100)
star("purple", 5, 50, 180, 100)
