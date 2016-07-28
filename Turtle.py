import turtle  # allows us to use the turtles library

wn = turtle.Screen()
wn.bgcolor("Blue")  # creates a graphics window
alex = turtle.Turtle()  # create a turtle named alex
alex.color("red")
alex.pensize(3)
alex.shape("turtle")
alex.up()

for i in range(1, 60, 2):
    alex.stamp()
    alex.forward(i)  # tell alex to move forward by 150 units
    alex.left(24)
    # turn by 90 degrees
wn.exitonclick()
