import pgzrun
HEIGHT=400
WIDTH=608
TITLE="starter"
boy=Actor("man")
boy.pos=(50,300)
def draw():
    screen.blit("background",(0,0))
    boy.draw()
pgzrun.go()