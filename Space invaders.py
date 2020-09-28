import turtle
import os
import random

win = turtle.Screen()
win.title("Space Invaders")
win.bgcolor("black")
win.setup(width=800, height=800)
win.tracer(0,0)

#Create spaceship
space = turtle.Turtle()
space.speed(0)
space.color("red")
space.shape("triangle")
space.penup()
space.setheading(90)            #try using space.lt(90)
space.goto(0,-350)


#Number of enemies
num_of_en=6
enemies = []                #an empty list of enemies

for i in range(num_of_en):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("blue")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.shapesize(1.5,1.5)
    x= random.randint(-300,300)
    y= random.randint(100,350)
    enemy.goto(x, y)
    enemy.dx = 0.2
    enemy.dy = 0.2



#Weapon
gun=turtle.Turtle()
gun.speed(0)
gun.color("yellow")
gun.shape("triangle")
gun.penup()
gun.setheading(90)
gun.shapesize(0.5, 0.5)
gun.hideturtle()
gun.dy = 0.5

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(300,350)

score =0

#See where the bullet is to fire one at a time
bullet = "yes"



#Functions
def space_r():
    x=space.xcor()
    x+=20
    if x > 380:
        x= 380
    space.setx(x)

def space_l():
    x=space.xcor()
    x-=20
    if x < -380:
        x= -380
    space.setx(x)

def gun_fire():
    global bullet                   # makes it a global variable
    if bullet == "yes":
        bullet="no"
        y=space.ycor() + 10
        x=space.xcor()
        gun.goto(x,y)
        gun.showturtle()




#Keyboard bindings
win.listen()
win.onkeypress(space_l, "Left")
win.onkeypress(space_r, "Right")
win.onkeypress(gun_fire, "space")




while True:
    win.update()

    #Move enemy
    for enemy in enemies:
        x=enemy.xcor()
        x+=enemy.dx
        enemy.setx(x)

        if enemy.xcor() > 380:
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            enemy.dx*=-1


        if enemy.xcor() < -380:
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            enemy.dx *= -1


        # Collision of bullet with enemy
        if gun.distance(enemy) < 20:
            gun.hideturtle()
            gun.goto(500, 500)
            bullet = "no"
            x = random.randint(-390, 390)
            y = enemy.ycor() + 80
            enemy.goto(x, y)
            score+=10
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=('Arial', 20, 'normal'))

        # Collision of enemy with space
        if space.distance(enemy) < 20:
            enemy.goto(200, 200)
            enemy.hideturtle()
            space.goto(0, -350)
            space.hideturtle()
            score = 0
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=('Arial', 20, 'normal'))

    #Move the bullet upwards
    if bullet == "no":
        y=gun.ycor()
        y+=gun.dy
        gun.sety(y)

    #To fire next bullet
    if gun.ycor() > 380:
        gun.hideturtle()
        bullet="yes"





