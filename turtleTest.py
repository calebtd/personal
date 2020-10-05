import turtle

t = turtle.Turtle()
t.shape("turtle")
t.width(1)
t.speed(10)

forward = 50
width = 2

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


# t.seth(10)
# t.circle(575, -20)
# # t.forward(200)
#
# move(-100, 150)
# t.seth(180)
# t.circle(150, 180)
#
# t.seth(10)
# t.circle(-575, 20)
# t.end_fill()
#
# move(-100, 150)
# t.seth(25)
# t.circle(-175, -115)
