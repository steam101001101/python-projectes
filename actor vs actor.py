import pgzrun
import random
HEIGHT=431
WIDTH=700
score=0
helldiver=Actor("helldiver")
helldiver.pos=(200,300)
creature=Actor("creature")
creature.pos=(200,300)
def draw():
    screen.blit("background",(0,0))
    screen.draw.text("score:"+str(score),center=(30,10))
    helldiver.draw()
    creature.draw()
def update():
    global score
    if helldiver.colliderect(creature):
        score=score+1
        creature.pos=random.randint(0,700),random.randint(0,431)
def on_mouse_down(pos):
    helldiver.pos=pos
def movememt():
    creature.pos=random.randint(0,700),random.randint(0,431)
    clock.schedule(movememt,1)
movememt()        
pgzrun.go()