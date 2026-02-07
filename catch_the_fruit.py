import pgzrun
import random
HEIGHT=405
WIDTH=603
score=0
basket=Actor("basket")
basket.pos=(250,350)
apple=Actor("apple")
apple.pos=(random.randint(50,603),35)
def draw():
    if score<0:
        screen.blit("end_of_the_road",(150,50))
        return
    screen.blit("ground",(0,0))
    screen.draw.text("score:"+str(score),center=(30,10))
    basket.draw()
    apple.draw()
def update():
    global score
    apple.y+=3
    if keyboard.d:
        basket.x+=5
    elif keyboard.a:
        basket.x-=5
    if basket.colliderect(apple):
        score=score+1
        apple.pos=(random.randint(50,603),35)
    if apple.y>405:
        apple.pos=(random.randint(50,603),35)
        score=score-1
pgzrun.go()