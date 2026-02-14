import pgzrun
import random
HEIGHT=405
WIDTH=603
score=0
basket=Actor("basket")
basket.pos=(250,350)
fruits=[]
images=["apple","orange","banana","watermelon",]
def new_fruit():
    fruit=Actor(random.choice(images))
    fruit.pos=(random.randint(50,550),10)
    fruits.append(fruit)
    clock.schedule(new_fruit,0.5)
bombs=[]
def new_bomb():
    bomb=Actor("bomb")
    bomb.pos=(random.randint(50,550),10)
    bombs.append(bomb)
    clock.schedule(new_bomb,10)
def draw():
    if score<0:
        screen.blit("end_of_the_road",(150,50))
        return
    screen.blit("ground",(0,0))
    screen.draw.text("score:"+str(score),center=(30,10))
    basket.draw()
    for fruit in fruits:
        fruit.draw()
    for bomb in bombs:
        bomb.draw()
def update():
    global score
    if score<0:
        return
    if keyboard.d:
        basket.x+=5
    elif keyboard.a:
        basket.x-=5
    for fruit in fruits:
        fruit.y+=2.5
        if basket.colliderect(fruit):
            score=score+1
            fruits.remove(fruit)
        if fruit.y>405:
            score=score-1
            fruits.remove(fruit)
new_fruit()
clock.schedule(new_bomb,10)
pgzrun.go()