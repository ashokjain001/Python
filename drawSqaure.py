import turtle
import time

def main():
    wn = turtle.Screen()
    ashok = turtle.Turtle()
    wn.bgcolor("darkslategray")
    ashok.color("yellow")
    ashok.pensize(3)
    ashok.speed(50)
    t = 0
    for i in range(20):
        t = t + 20
        multisquare(ashok,t)
        ashok.penup()
        ashok.right(135)
        ashok.forward(14.14)
        ashok.left(135)
        ashok.pendown()
    wn.exitonclick()

def multisquare(t,size):
    for i in range(4):
        t.forward(size)
        t.left(90)
print main()