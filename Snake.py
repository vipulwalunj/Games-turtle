#Snake game

import turtle
import time

delay = 0.1
import random



win=turtle.Screen()
win.title("Vipul")
win.bgcolor("blue")
win.setup(width=800, height=800)
win.tracer(0,0)      #Turns off the screen updates


#snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('red')
snake.penup()
snake.goto(0,0)
snake.direction= "stop"

segment = []

#Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('black')
food.penup()
food.goto(0,100)

score = 0
high=0

#Scorecard
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)



#Functions

def move_up():
    if snake.direction != "down":
        snake.direction="up"
def move_down():
    if snake.direction != "up":
        snake.direction="down"
def move_right():
    if snake.direction != "left":
        snake.direction="right"
def move_left():
    if snake.direction != "right":
        snake.direction="left"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        y+=20
        snake.sety(y)
    if snake.direction == "down":
        y = snake.ycor()
        y-=20
        snake.sety(y)
    if snake.direction == "right":
        x = snake.xcor()
        x+=20
        snake.setx(x)
    if snake.direction == "left":
        x = snake.xcor()
        x-=20
        snake.setx(x)



#Keyboard binding
win.listen()
win.onkeypress(move_up, 'Up')
win.onkeypress(move_down,'Down')
win.onkeypress(move_right,'Right')
win.onkeypress(move_left,'Left')



#Main loop
while True:
    win.update()                            #Very very important

    #Borders
    if snake.xcor() > 390 or snake.xcor() < -390 or snake.ycor() > 390 or snake.ycor() < -390:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction="stop"

        # Remove segments
        for i in segment:
            i.goto(1000, 1000)      # Takes the segment out of the window

        #Clear segments
        segment.clear()             # CLears the segments behind the head of the snake
        score=0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high), align="center", font=("Arial", 24, "normal"))


    #Collision with food
    if snake.distance(food) < 15:           # to find distance between two
        #Moves food to a random place
        x = random.randint(-390,390)        #Assigns a random value in the given range
        y = random.randint(-390,390)
        food.goto(x,y)

        # Add a segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("red")
        new_seg.penup()
        segment.append(new_seg)

        #Increase the Score
        score+=1
        if score > high:
            high = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high), align="center", font=("Arial", 24, "normal"))

    #Move segments
    for index in range(len(segment)-1, 0, -1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x, y)

    #Move segment 0 to where head is
    if len(segment) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x, y)

    move()

    #CHeck for body collisions
    for i in segment:
        if i.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"

            for i in segment:
                i.goto(1000, 1000)
            segment.clear()

            score=0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high), align="center", font=("Arial", 24, "normal"))

    time.sleep(delay)