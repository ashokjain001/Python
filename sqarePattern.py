import turtle

wn = turtle.Screen()
ashok = turtle.Turtle()
ashok.pensize(3)

def sqaurePattern():
    for j in range(4):
        ashok.forward(40)
        ashok.left(90)
    ashok.left(22.5)


for i in range(16):
    sqaurePattern()

wn.exitonclick()
