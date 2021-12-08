import turtle

wind=turtle.Screen()
wind.title=('ping pong game')
wind.bgcolor("green")
wind.setup(width=800,height=600)
wind.tracer(0)

leftpaddle=turtle.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

rightpaddle=turtle.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

pen=turtle.Turtle()
pen.speed(0)
pen.color("aqua")
pen.up()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=('arial',26,'normal'))


score_a = 0
score_b = 0


#moving the left paddle
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)    

#moving the right paddle
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)  

#assigning keys to play
wind.listen()
wind.onkeypress(leftpaddleup,'q')
wind.onkeypress(leftpaddledown,'a')
wind.onkeypress(rightpaddleup,'Up')
wind.onkeypress(rightpaddledown,'Down')

while True:
    wind.update()

    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

     #score
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
        ball.goto(0,0)
        ballxdirection *= -1
    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B {}".format(score_a, score_b), align='center',
                     font=('Courier', 24, 'normal'))
        ball.goto(0, 0)
        ballxdirection *= -1
    

    #collisions with borders
    if ball.xcor() < -340 and ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50:
        ballxdirection *= -1
    elif ball.xcor() > 340 and ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50:
        ballxdirection *= -1

    if(score_a==5 or score_b==5):
        if(score_a>score_b):
          pen.goto(0,0)
          pen.write("PLAYER A WINS" , move = False, align="center" ,font=("Arial" , 30 ,"normal") )
        else:
            pen.goto(0,0)
            pen.write("PLAYER B WINS" , move = False, align="center" ,font=("Arial" , 30 ,"normal") )
        
    