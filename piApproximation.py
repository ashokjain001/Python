import turtle
import math
import random

fred = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-1, -1, 1, 1)
fred.speed(10)

fred.up()

insideCount = 0
numdarts = 50000
for i in range(numdarts):
    randx = random.uniform(-1, 1)
    randy = random.uniform(-1, 1)

    x = randx
    y = randy
    fred.up()
    fred.goto(x, y)

    if fred.distance(0, 0) < 1:
        #fred.color("red")
        #fred.dot()
        insideCount = insideCount + 1
    #else:
        #fred.color("blue")
        #fred.dot()

        # fred.up()

print(insideCount, numdarts)
print float((insideCount / numdarts) * 4)

wn.exitonclick()