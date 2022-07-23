#imported turtel module
import turtle

wind = turtle.Screen() #intializes screen
wind.title('Ping Pong by Ammar') #set the title of the window
wind.bgcolor(.1,.1,.1) #set the background color of the window
wind.setup(width=800, height=600) #set the width and height of the window
wind.tracer(0) #stops the window from updating automatically

#Madrab1
madrab1 = turtle.Turtle() #intializes turtle object(shape)
madrab1.speed(0) #set the speed of the animation
madrab1.shape('square') #set the shape of the object
madrab1.color('blue') #set the color of the shape
madrab1.shapesize(stretch_wid=5, stretch_len=1) #stretches the shape to meet size
madrab1.penup() #stops the object from drawing lines
madrab1.goto(-360,0) #set the position of the object

#Madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape('square')
madrab2.color('red')
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align='center', font=('courier',18,"normal"))

#Center line
cel = turtle.Turtle()
cel.speed(0)
cel.shape('square')
cel.color('white')
cel.shapesize(stretch_len=.1 , stretch_wid=25)
cel.penup()
cel.goto(0,0)

#functions

mspeed = 17

def madrab1_up():
    y = madrab1.ycor()
    y += mspeed
    madrab1.sety(y)


def madrab1_down():
    y = madrab1.ycor() #get the y coordinate of the madrab
    y -= mspeed #set the y to increase be 20
    madrab1.sety(y) #set the y of the madrab1 to the new y coordinate

def madrab2_up():
    y = madrab2.ycor()
    y += mspeed
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y -= mspeed
    madrab2.sety(y)

#keyboard bindings
wind.listen() #tell the window to expect keyboard input
wind.onkeypress(madrab1_up, "w") #when pressing w the function madrab1_up is invoked
wind.onkeypress(madrab1_down, "s") 
wind.onkeypress(madrab2_up, 'Up')
wind.onkeypress(madrab2_down, 'Down')

#main game loop
while True:
    wind.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops run--->+0.4 xaxis
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loops run--->+0.4 xaxis

    #border check , top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() >290: #if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction, making +0.3--->-0.3

    if ball.ycor() <-290: #if ball is at bottom border
        ball.sety(-290) #set y coordinate -290
        ball.dy *= -1 #reverse direction, making +0.3--->-0.3

    if ball.xcor() >390: #if ball is at right border
        ball.goto(0,0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align='center', font=('courier',18,"normal"))

    if ball.xcor() <-390: #if ball is at left border
        ball.goto(0,0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align='center', font=('courier',18,"normal"))

    #tasadom madrab and ball
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() +50 and ball.ycor() > madrab2.ycor() -50):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() +50 and ball.ycor() > madrab1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

