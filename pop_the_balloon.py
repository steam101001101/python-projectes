import turtle
import random
screen=turtle.Screen()
screen.setup(500,500)
screen.bgcolor("lightblue")
pointer=turtle.Turtle()
pointer.shape("triangle")
pointer.color("black")
pointer.penup()
pointer.left(90)
pointer.backward(230)
def right():
    pointer.setx(pointer.xcor()+25)
def left():
    pointer.setx(pointer.xcor()-25)
screen.listen()
screen.onkey(right,"d")
screen.onkey(left,"a")
def balloons():
    balloon=turtle.Turtle()
    balloon.hideturtle()
    balloon.shape("circle")
    colour=["red","green","blue","purple","yellow","brown","orange"]
    balloon.color(random.choice(colour))
    balloon.penup()
    y=(200)
    x=random.randint(-200,200)
    balloon.goto(x,y)
    balloon.showturtle()
    return balloon
balloon=balloons()
score=0
speed=2.5
while True:
    balloon.sety(balloon.ycor()-speed)
    if score==10:
        speed=3
    if score<0:
        turtle.clear()
        turtle.goto(0,0)
        turtle.write("game over",font=("arial",50,"bold"))
        break
    if balloon.ycor()<-240:
        balloon.hideturtle()
        balloon=balloons()
        score=score-1
        turtle.clear()
        turtle.write("score:"+str(score),font=("arial",20,"bold"))
    if pointer.distance(balloon)<20:
        turtle.penup()
        turtle.goto(250,250)
        score=score+1
        turtle.clear()
        turtle.write("score:"+str(score),font=("arial",20,"bold"))
        balloon.hideturtle()
        balloon=balloons()
turtle.exitonclick()