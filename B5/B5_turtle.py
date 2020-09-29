import turtle

forward = 50
width = 2

t = turtle.Turtle()
t.shape("turtle")
t.width(1)
t.speed(10)

x = 1

t.up()
t.goto(0, 0)
t.down()

# for c in ['red', 'green', 'yellow', 'blue']:
#    t.color(c)
#    t.forward(forward)
#    t.left(90)

t.write("hello", move=False, align='center', font=('Arial', 50, 'normal'))

# while True:
#   t.color("orange")
#   t.forward(forward + x)
#   t.left(100)
#   x += 1

turtle.exitonclick()
