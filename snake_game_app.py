# Snake Game 

import turtle
import time
import random

delay = 0.1 

# Score Varibales

score = 0
high_score = 0

# Screen setup
wn = turtle.Screen()
wn.title("Snake Game by Andy Adofo")
wn.bgpic("checkerboardblue.gif")
wn.setup(width=600, height=600)
wn.tracer(0) #Keeps the screen turned off

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,0)


segments = []

# Score table
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))



# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":    
        head.direction = "right"            

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)   

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)             

#Keyboard inputs
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")





# Main game loop
while True:
    wn.update()

    # Border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hiding segments
        for segment in segments:
            segment.goto(1000, 1000)

        #Clear segments
        segments.clear()

        # Reset score
        score = 0


        
        #Updateing score when head collides
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



    if head.distance(food) < 20:
        # move food to another location
        x = random.randint(-285,285)
        y = random.randint(-285,285)
        food.goto(x,y)

        #Making body longer as it eats
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten delay
        delay -= 0.001

        # Increasing score
        score = score + 10

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))





    # Moving segments in rev order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to the location of head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    #Head collisaion with body 

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hiding segments
            for segment in segments:
             segment.goto(1000, 1000)

            #Clear segments
            segments.clear()

    time.sleep(delay)

wn.mainloop()