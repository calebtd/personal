import turtle

t = turtle.Turtle()


def move(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


t.width(2)
move(0, -125.75)

t.speed(500)
t.color("black", "orange")
t.begin_fill()

t.seth(325)
t.circle(150, 250)
print(t.pos())
t.seth(145)
t.circle(150, 250)

t.end_fill()
t.width(1)

move(-130, 140)
t.seth(225)
t.circle(203, 90)

move(-65, 145)
t.seth(225)
t.circle(210, 90)

move(0, 200)
t.seth(-90)
t.forward(400)

turtle.exitonclick()
