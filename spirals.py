import turtle

wn = turtle.Screen()
ashok = turtle.Turtle()
ashok.speed(50)
wn.bgcolor("darkslategray")
ashok.color("yellow")

t = 0
for i in range(50):
    t = t+10
    ashok.forward(t)
    ashok.left(91)

wn.exitonclick()