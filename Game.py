import turtle

turtle.title("Tic-tac-toe")  # Setting the title
window = turtle.Screen() # For screen object
global i
i = 0

#Defining a turtle
def define_turtle(pcolor = "white", pspeed = 1, pwidth = 2, x = 0, y = 0, pshape = "arrow"):
    pname = turtle.Turtle()
    pname.up()
    pname.color(pcolor)
    pname.speed(pspeed)
    pname.width(pwidth)
    pname.setposition(x, y)
    pname.shape(pshape)
    return pname

# Display window manipulation
turtle.setup(600, 600)
turtle.bgcolor("black")

# 2 Turtles to control the row/column and the players
rowCircleTurtle = define_turtle(pspeed = 5, pwidth = 5, x = -300, y = 100)
columnCrossTurtle = define_turtle(pcolor = "yellow", pwidth = 5, pspeed = 5, x = -100, y = 300)

# 2 Clone Turtles to draw the 2nd row/column
rowCircleTurtle1 = rowCircleTurtle.clone()
columnCrossTurtle1 = columnCrossTurtle.clone()

columnCrossTurtle.down()
columnCrossTurtle.right(90)
columnCrossTurtle.forward(600)

columnCrossTurtle1.setposition(100, 300)
columnCrossTurtle1.down()
columnCrossTurtle1.right(90)
columnCrossTurtle1.forward(600)

rowCircleTurtle.down()
rowCircleTurtle.forward(600)

rowCircleTurtle1.setposition(-300, -100)
rowCircleTurtle1.down()
rowCircleTurtle1.forward(600)

# Creating centre of each box to have a proper input
centerTurtle = define_turtle(pcolor = "#3F403D", pspeed = 0, pwidth = 5, pshape = "turtle", x = -200, y = 200)
adjust = 200

for i in range(3):
    for j in range(3):
        centerTurtle.begin_fill()
        centerTurtle.circle(15)
        centerTurtle.end_fill()
        centerTurtle.setx(-200 + adjust)
        adjust += 200
    adjust = 200
    centerTurtle.setposition(-200, 200 - (i + 1) * adjust)

centerTurtle.color("green")

# To get the proper square
def fxn(x, y):
    if -298.0 < x < -117.0:
        centerTurtle.setx(-200)
    elif -73.0 < x < 83.0:
        centerTurtle.setx(0)
    elif 115.0 < x < 272.0:
        centerTurtle.setx(200)
    if 109.0 < y < 293.0:
        centerTurtle.sety(200)
    elif -84.0 < y < 82.0:
        centerTurtle.sety(0)
    elif -276.0 < y < -119.0:
        centerTurtle.sety(-200)
    global i
    if i % 2 == 0:
        draw_circle(centerTurtle.xcor(), centerTurtle.ycor())
    else:
        draw_cross(centerTurtle.xcor(), centerTurtle.ycor())
    i += 1
        

# Draw circle or cross
def draw_circle(x, y):
    circleTurtle = define_turtle(pcolor = "white", pspeed = 10, pwidth = 7)
    circleTurtle.hideturtle()
    circleTurtle.setposition(x, y - 50)
    circleTurtle.down()
    circleTurtle.circle(65)
    circleTurtle.up()

def draw_cross(x, y):
    crossTurtle = define_turtle(pcolor = "white", pspeed = 10, pwidth = 8)
    crossTurtle.hideturtle()
    crossTurtle.setposition(x - 20, y)
    crossTurtle.down()
    crossTurtle.left(45)
    crossTurtle.forward(100)
    crossTurtle.backward(160)
    crossTurtle.up()
    crossTurtle.setposition(x - 50, y + 70)
    crossTurtle.down()
    crossTurtle.right(90)
    crossTurtle.forward(160)
    crossTurtle.up()

# Determine the turn
##def det_turn(x, y):
##    if count % 2:
##        draw_circle(x, y)
##    else:
##        draw_cross(x, y)
##    count += 1
window.onclick(fxn)




