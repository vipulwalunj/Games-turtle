#Pong Game

import turtle               # For easy games
win = turtle.Screen()       # we get a separate window named 'win'
win.title("Vipul's game")
win.bgcolor("black")
win.setup(width=800, height=600)    #Gives dimensions to the window
win.tracer(0)                       #speed up our game

#score
score_1=0
score_2=0

#Bar 1
bar_1 = turtle.Turtle()  #create a turtle(object) named bar_1
bar_1.speed(0)           # Not for the actual speed just a necessary command
bar_1.shape("square")
bar_1.color("white")
bar_1.shapesize(stretch_wid=5,stretch_len=1)    # By default turtle size is 20 by 20
bar_1.penup()                                   # Will move around the screen but will not draw
bar_1.goto(-350,0)


#Bar 2
bar_2 = turtle.Turtle()
bar_2.speed(0)
bar_2.shape("square")
bar_2.color("white")
bar_2.shapesize(stretch_wid=5,stretch_len=1)
bar_2.penup()
bar_2.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2         # Ball moves by 2 pixels
ball.dy = -0.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)





#Function
def bar_1_up():
    y = bar_1.ycor()            #ycor returns the y coordinate
    y += 20
    bar_1.sety(y)               # Sets the y coordinate to new y parameter

def bar_1_down():
    y = bar_1.ycor()
    y -= 20
    bar_1.sety(y)

def bar_2_up():
    y = bar_2.ycor()
    y += 20
    bar_2.sety(y)

def bar_2_down():
    y = bar_2.ycor()
    y -= 20
    bar_2.sety(y)

#Keyboard binding
win.listen()                    # command for it to listen to the keyboard
win.onkeypress(bar_1_up, 'w')   # When user presses 'w' it passes the function
win.onkeypress(bar_1_down, 's')
win.onkeypress(bar_2_up, 'Up')      #'Up' indicates the up arrow
win.onkeypress(bar_2_down, 'Down')  #'Down' indicates the down arrow


#Main game Loop
while True:
    win.update()     # Everytime the loop runs it updates the screen

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()                 #clears what is written on the screen
        pen.write("Player 1: {}    Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 20, "normal"))

    # Collisions
    if ball.xcor() > 340 and ball.xcor() <350 and (ball.ycor() > bar_2.ycor() -50) and (ball.ycor() < bar_2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() > bar_1.ycor() -50) and (ball.ycor() < bar_1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    if score_2 == 3:
        pen.clear()
        pen.write("Player 2 wins", align="center", font=("Arial", 20, "normal"))
        ball.goto(0, 0)
        ball.dx=0
        ball.dy=0

    if score_1 == 3:
        pen.clear()
        pen.write("Player 1 wins", align="center", font=("Arial", 20, "normal"))
        ball.goto(0, 0)
        ball.dx=0
        ball.dy=0

