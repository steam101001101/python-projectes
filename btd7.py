import pgzrun
import random
HEIGHT=431
WIDTH=700
george=Actor("george")
george.pos=(200,300)
bloon=Actor("theredbloon")
bloon.pos=(500,300)
def draw():
    screen.blit("background",(0,0))
    george.draw()
    bloon.draw()
def on_mouse_down(pos):
    if george.collidepoint(pos):
        george.pos=random.randint(0,700),random.randint(0,431)
pgzrun.go()