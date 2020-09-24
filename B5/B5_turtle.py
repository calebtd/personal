import turtle

forward = 100
width = 2

t = turtle.Turtle()
t.shape("turtle")
t.width(5)

t.up()
t.goto(-50, -50)
t.down()

for c in ['red', 'green', 'yellow', 'blue']:
    t.color(c)
    t.forward(forward)
    t.left(90)

turtle.exitonclick()
