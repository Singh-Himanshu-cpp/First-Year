#imports
import os
import turtle
import time
import random

delay = 0.05

# level of the player
level=1

#scores
score = 0
path_cwd=os.getcwd()
path_score=path_cwd+"\score.txt"
if(os.path.isfile(path_cwd+"\score.txt")):
    f1=open("score.txt","r")
    high_score = int(f1.readline())
    f1.close()
else:
    f1=open("score.txt","w")
    f1.write("0")
    high_score=0
    f1.close()

#set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('light green')
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake eyes

# left
eye_left = turtle.Turtle()
eye_left.speed(0)
eye_left.shape("square")
eye_left.color("black")
eye_left.penup()
eye_left.goto(-5,0)
eye_left.shapesize(0.3,0.3,1)
# right
eye_right = turtle.Turtle()
eye_right.speed(0)
eye_right.shape("square")
eye_right.color("black")
eye_right.penup()
eye_right.goto(5,0)
eye_right.shapesize(0.3,0.3,1)  

#snake food
food= turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

# snake body
segments = []

#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0  High score: "+str(high_score), align = "center", font=("ds-digital", 24, "normal"))

#Functions
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
        x = head.xcor()
        y = head.ycor()
        head.sety(y+20)
        # setting eyes
        eye_left.sety((y+20))
        eye_right.sety((y+20))
        eye_left.setx((x-5))
        eye_right.setx((x+5))
    if head.direction == "down":
        x = head.xcor()
        y = head.ycor()
        head.sety(y-20)
        # setting eyes
        eye_left.sety((y-20))
        eye_right.sety((y-20))
        eye_left.setx((x+5))
        eye_right.setx((x-5))
    if head.direction == "left":
        x = head.xcor()
        y = head.ycor()
        head.setx(x-20)
        # setting eyes
        eye_left.sety((y-5))
        eye_right.sety((y+5))
        eye_left.setx((x-20))
        eye_right.setx((x-20))
    if head.direction == "right":
        x = head.xcor()
        y = head.ycor()
        head.setx(x+20)
        # setting eyes
        eye_left.sety((y-5))
        eye_right.sety((y+5))
        eye_left.setx((x+20))
        eye_right.setx((x+20))

def stop(head,eye_left,eye_right,sc):
    time.sleep(1)
    head.goto(0,0)
    eye_left.goto(-5,0)
    eye_right.goto(5,0)
    head.direction = "stop"
def stop2(head,eye_left,eye_right,sc,l1,l2,b1,b2):
    time.sleep(1)
    head.goto(0,0)
    eye_left.goto(-5,0)
    eye_right.goto(5,0)
    head.direction = "stop"
    l1.goto(1000,1000)
    l2.goto(1000,1000)
    b1.goto(1000,1000)
    b2.goto(1000,1000)

    #hide segments
    for segment in segments:
        segment.goto(1000,1000)
    segments.clear()

    #update the score     
    f=open("score.txt","w")
    f.write(str(high_score))
    f.close()
    sc.clear()
    sc.write("score: {}  High score: {}".format(0,high_score), align="center", font=("ds-digital", 24, "normal"))
#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#MainLoop
while True:
    wn.update()
    if level==1:
        # passing snake through border area
        if head.xcor()>290 or head.xcor()<-290:
            head.setx(-head.xcor()*0.9)
        if head.ycor()>290 or head.ycor()<-290:
            head.sety(-head.ycor()*0.9)
    elif level==2:
        if head.xcor()>270 or head.xcor()<-270 or head.ycor()>270 or head.ycor()<-270:
            score = 0
            delay = 0.05
            level=1
            stop2(head,eye_left,eye_right,sc,l1,l2,b1,b2)

    #check collision with food
    if head.distance(food) <20:
        # move the food to random place
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)

        #add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
        new_segment.goto(1000,1000)

        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10
        # increasing the level
        if score==200:
            level=2
            delay += 0.004

            # adding boundaries
            l1=turtle.Turtle()
            l1.speed(0)
            l1.shape("square")
            l1.shapesize(stretch_len=1,stretch_wid=30)
            l1.penup()
            l1.goto(-295,0)
            l2=turtle.Turtle()
            l2.speed(0)
            l2.shape("square")
            l2.shapesize(stretch_len=1,stretch_wid=30)
            l2.penup()
            l2.goto(290,0)
            b1=turtle.Turtle()
            b1.speed(0)
            b1.shape("square")
            b1.shapesize(stretch_len=30,stretch_wid=1)
            b1.penup()
            b1.goto(0,295)
            b2=turtle.Turtle()
            b2.speed(0)
            b2.shape("square")
            b2.shapesize(stretch_len=30,stretch_wid=1)
            b2.penup()
            b2.goto(0,-290)
            sc.goto(0,240)

            # writing reached to level 2
            writer = turtle.Turtle()
            writer.hideturtle()
            writer.color("black")
            writer.penup()
            writer.goto(0,0)
            writer.write("Level 2", align = 'center', font = ('Arial', 32, 'normal'))
            wn.update()
            time.sleep(2)
            writer.clear()


        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 

    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            score = 0
            delay = 0.05
            if level==1:
                stop(head,eye_left,eye_right,sc)
            elif level==2:
                level=1
                stop2(head,eye_left,eye_right,sc,l1,l2,b1,b2)
    
    time.sleep(delay)
wn.mainloop()