import random
import turtle
ashok = turtle.Turtle()
deepika = turtle.Turtle()
bn = turtle.Screen()
bn.bgcolor("Blue")
deepika.color("yellow")
ashok.color("red")

def test():

     if (random.random()) > 0.1:
         return True
     else:
         return False


while test():
    angle = random.randrange(0, 100)
    angle2 = random.randrange(0,100)
    coin = random.randrange(0,2)
    if coin == 0 :
        ashok.left(angle)
        deepika.left(angle2)

    else:
        ashok.right(angle)
        deepika.right(angle2)

    ashok.forward(50)
    deepika.forward(50)

bn.exitonclick()