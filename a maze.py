import turtle
screen=turtle.Screen()
screen.setup(700,500)
screen.bgcolor("green")
pen=turtle.Turtle()
pen.shape("turtle")
maze=[
    "xxxxxxxxxxxx",
    "x  x    x  x",
    "x  x  x   xx",
    "x  xx xxxxxx",
    "xx         x",
    "xx xxxxxxx x",
    "xx x  xxx  x",
    "xx x xxxx xx",
    "xx   xx   xx",
    "x    xx    x",
    "xxxx xx xxxx",
    "xx        fx",
    "xxxxxxxxxxxx"
]
tiles=[]
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x]=="x":
            tile=turtle.Turtle()
            tile.up()
            tile.shape("square")
            tilex=-288+(x*24)
            tiley=288-(y*24)
            tile.goto(tilex,tiley)
            tiles.append(tile)
        elif maze[y][x]=="f":
            food=turtle.Turtle()
            food.up()
            food.shape("circle")
            food.color("blue")
            foodx=-288+(x*24)
            foody=288-(y*24)
            food.goto(foodx,foody)
pen.up()
pen.goto(-264,264)
def right():
    x=pen.xcor()+24
    y=pen.ycor()
    if valid_move(x,y):
        pen.goto(x,y)
def left():
    x=pen.xcor()-24
    y=pen.ycor()
    if valid_move(x,y):
        pen.goto(x,y)
def up():
    x=pen.xcor()
    y=pen.ycor()+24
    if valid_move(x,y):
        pen.goto(x,y)
def down():
    x=pen.xcor()
    y=pen.ycor()-24
    if valid_move(x,y):
        pen.goto(x,y)
def valid_move(x,y):
    for tile in tiles:
        if x==tile.xcor() and y==tile.ycor():
            return False
    return True
screen.listen()
screen.onkey(right,"d")
screen.onkey(left,"a")
screen.onkey(up,"w")
screen.onkey(down,"s")
while True:
    if pen.distance(food)<10:
        food.write("you won",font=("arial",20,"bold"))
        break
  