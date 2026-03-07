import pgzrun
HEIGHT=400
WIDTH=600
ship=Actor("space_ship")
ship.pos=(300,350)
enemy_list=[]
bullets=[]
def enemies():
    for i in range(3):
        enemy=Actor("enemy_ship")
        enemy.x=i*120+35
        enemy.y=20
        enemy_list.append(enemy)
        clock.schedule(enemies,5)
def draw():
    screen.blit("space",(0,0))
    ship.draw()
    for enemy in enemy_list:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("player_bullet")
        bullet.pos=(ship.x,350)
        bullets.append(bullet)
def update():
    if keyboard.d:
        ship.x+=5
    elif keyboard.a:
        ship.x-=5
    for enemy in enemy_list:
        enemy.y+=0.5
        if enemy.y>400:
            enemy_list.remove(enemy)
    for bullet in bullets:
        bullet.y-=1
        if bullet.y<0:
            bullets.remove(bullet)
enemies()
pgzrun.go()