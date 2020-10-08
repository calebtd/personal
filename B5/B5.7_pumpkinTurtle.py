import turtle

# initial setup
t = turtle.Turtle()
turtle.bgcolor('#2b2b2b')
t.speed(500)


# make a move function for pen up and down
def move(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


# stem
t.color('green')
move(20, 110)
t.seth(70)
t.begin_fill()
t.circle(75, 120)
t.seth(-40)
t.circle(-75, 120)
t.end_fill()

# set width and move to start
t.width(3)
move(0, -125.75)

# colors
t.color('black', 'orange')
t.begin_fill()

# shape of pumpkin
t.seth(325)
t.circle(150, 250)
print(t.pos())
t.seth(145)
t.circle(150, 250)
t.end_fill()

t.width(1)

########################
# left lines
heading = 225

move(-130, 140)
t.seth(heading)
t.circle(203, 90)

move(-65, 145)
t.seth(heading)
t.circle(210, 90)

move(-8, 123)
t.seth(heading)
t.circle(180, 90)
########################
# right lines
move(130, 140)
t.seth(-heading)
t.circle(203, -90)

move(65, 145)
t.seth(-heading)
t.circle(210, -90)

move(8, 123)
t.seth(-heading)
t.circle(180, -90)
########################


# move(0, 200)
# t.seth(-90)
# t.forward(400)

turtle.done()
