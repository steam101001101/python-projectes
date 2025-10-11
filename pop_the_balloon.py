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
while True:
    balloon.sety(balloon.ycor()-2.5)
    if balloon.ycor()<-240:
        balloon.hideturtle()
        balloon=balloons()
    if pointer.distance(balloon)<20:
        balloon.hideturtle()
        balloon=balloons()
turtle.exitonclick()