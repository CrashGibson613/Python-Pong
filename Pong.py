
import turtle

#booleans to disable paddle movement when they are at the edge
canMoveUp = True
canMoveDown = True
canMoveUpB = True
canMoveDownB = True

# Window setup

wnd = turtle.Screen()
wnd.title("Fortnite 1972 Edition")
wnd.bgcolor("black")
wnd.setup(width = 800, height = 600)
#Without tracer, the game runs very slow
wnd.tracer(0)

#Middle line
#turtle.Turtle calls a class that draws lines to make a sprite
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid= 100, stretch_len= 0.1)
paddleB.goto(0, 0)

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid= 5, stretch_len= 1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid= 5, stretch_len= 1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
#The ball is drawn last so it is rendered over everything, such as the center line  
ball = turtle.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.color("white")
ball.shapesize(stretch_wid= 1.5, stretch_len= 1.55)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.24
ball.dy = 0.24

#pen lets us draw the scores, we hide it with hideturtle()
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("0               0",align="center", font=("Corier", 40, "normal"))

#Score
scoreA = 0
scoreB = 0
# Functions
def paddleAUp():
    if canMoveUp == True:
        y = paddleA.ycor()
        y += 20
        paddleA.sety(y)

def paddleADown():
    if canMoveDown == True:
        y = paddleA.ycor()
        y -= 20
        paddleA.sety(y)

def paddleBUp():
    if canMoveUpB == True:
        yb = paddleB.ycor()
        yb += 20
        paddleB.sety(yb)

def paddleBDown():
    if canMoveDownB == True:
        yb = paddleB.ycor()
        yb -= 20
        paddleB.sety(yb)

# Keyboard bindings
wnd.listen()
wnd.onkeypress(paddleAUp, "w")
wnd.onkeypress(paddleADown, "s")

wnd.onkeypress(paddleBUp, "Up")
wnd.onkeypress(paddleBDown, "Down")


# Main game loop

while True:
    wnd.update()

    # Border checking

    # Top and bottom 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    if paddleA.ycor() > 255:
        canMoveUp = False
    else:
        canMoveUp = True
    if paddleB.ycor() > 255:
        canMoveUpB = False
    else:
        canMoveUpB = True


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    if paddleA.ycor() < -255:
        canMoveDown = False
    else:
        canMoveDown = True
    if paddleB.ycor() < -255:
        canMoveDownB = False
    else:
        canMoveDownB = True
    

    #Right and left

    if ball.xcor() > 399:
        scoreA += 1
        pen.clear()
        pen.write("{}               {}".format(scoreA, scoreB), align="center", font=("Corier", 40, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -399:
        scoreB += 1
        pen.clear()
        pen.write("{}               {}".format(scoreA, scoreB), align="center", font=("Corier", 40, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    
    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle and ball collisions
    if ball.xcor() < - 340 and ball.xcor() < -350 and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
