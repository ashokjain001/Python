import turtle


def main(sides,length):
    wn = turtle.Screen()
    ashok = turtle.Turtle()
    wn.bgcolor("darkslategray")
    ashok.color("yellow")
    ashok.pensize(4)
    polygon(ashok,sides,length)
    wn.exitonclick()



def polygon(t,sides,length):

    degree = 360/sides
    for i in range(sides):
        t.forward(50)
        t.left(degree)

main(8,50)