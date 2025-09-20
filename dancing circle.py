import turtle
import random
import time
screen=turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(100)
pen.color("green")
colour=["red","green","blue","white","yellow","purple"]
def circle():
  pen.color(random.choice(colour))
  size=random.randint(50,100)
  pen.begin_fill()
  pen.circle(size)
  pen.end_fill()
for i in range(50):
  x=random.randint(-200,200)
  y=random.randint(-200,200)
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  circle()
  time.sleep(0.25)
  pen.clear()