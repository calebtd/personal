# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Common ACT Math Problems Assignment
# I did not copy anyone

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
move(27, 110)
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
# eyes
t.color('#141414')
ex = 75
ey = 110
move(-ex, ey)
t.seth(180)
t.begin_fill()
t.circle(50, 360, 3)
t.end_fill()
move(ex, ey)
t.begin_fill()
t.circle(50, 360, 3)
t.end_fill()

#########################
# nose
move(0, 30)
t.begin_fill()
t.circle(25, 360, 3)
t.end_fill()

#########################
# mouth
t.color('#141414')
t.width(2)
move(-150, -35)
t.begin_fill()
t.seth(0)
t.forward(300)
t.seth(230)
t.circle(-195, 100, 4)
t.end_fill()
#########################
# animation
t.color('black')
t.width(1)
t.speed(10000)

t.seth(-50)
move(-1000, 500)
for lines in range(250):
    move(-1000 + (lines * 5), 500)
    t.forward(1000)

turtle.done()
