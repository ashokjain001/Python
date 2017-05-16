import turtle

def turtlenew():

    w = turtle.Screen()
    w.bgcolor("green")

    tur = turtle.Turtle()
    tur.shape("turtle")
    tur.color("yellow")



    for i in range(20):

        for i in range(4):
            tur.forward(100)
            tur.right(90)
        tur.right(20)


    w.exitonclick()

print turtlenew()