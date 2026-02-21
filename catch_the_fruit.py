import pgzrun
import random
HEIGHT=405
WIDTH=603
score=0
basket=Actor("basket")
basket.pos=(250,350)
fruits=[]
images=["apple","orange","banana","watermelon",]
start=False
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
    clock.schedule(new_bomb,random.randint(1,5))
def draw():
    if score<0:
        screen.blit("end_of_the_road",(150,50))
        return
    screen.blit("ground",(0,0))
    screen.draw.text("score:"+str(score),center=(30,10))
    if start==False:
        screen.draw.text("PRESS THE ENTER KEY TO START",center=(WIDTH//2,HEIGHT//2),fontsize=50)
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
    for bomb in bombs:
        bomb.y+=1.5
        if basket.colliderect(bomb):
            score=score-50
            bombs.remove(bomb)
        if bomb.y>405:
            bombs.remove(bomb)
def on_key_down(key):
    global start
    if key==keys.RETURN:
        start=True
        new_fruit()
        clock.schedule(new_bomb,random.randint(1,5))
pgzrun.go()