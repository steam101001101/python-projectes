import pgzrun
HEIGHT=400
WIDTH=600
ship=Actor("space_ship")
ship.pos=(300,350)
enemy_list=[]
def enemies():
    for i in range(5):
        enemy=Actor("enemy_ship")
        enemy.x=i*120+35
        enemy.y=20
        enemy_list.append(enemy)
def draw():
    screen.blit("space",(0,0))
    ship.draw()
    for enemy in enemy_list:
        enemy.draw()
def update():
    if keyboard.d:
        ship.x+=5
    elif keyboard.a:
        ship.x-=5
enemies()
pgzrun.go()