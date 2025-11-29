import random
gridA=[[" "," "," "," "," "],
       [" "," "," "," "," "],
       [" "," "," "," "," "],
       [" "," "," "," "," "],
       [" "," "," "," "," "]]
for i in range(3):
    number1=random.randint(0,4)
    number2=random.randint(0,4)
    gridA[ number1][number2]="*"
"""for row in gridA:
    print("|".join(row))
    print("_________")"""
gridB=[[" "," "," "," "," "],
       [" "," "," "," "," "],
       [" "," "," "," "," "],
       [" "," "," "," "," "],
       [" "," "," "," "," "]]
for i in range(3):
    shipr=int(input("what row number"))
    shipc=int(input("what col number"))
    gridB[shipr][shipc]="^"
for row in gridB:
    print("|".join(row))
    print("_________")
while True:
    guestrow=int(input("guess the row"))
    guestcol=int(input("guess the col"))
    if gridA[guestrow][guestcol]=="*":
        gridA[guestrow][guestcol]="x"
        print("SHIP DOWN")
    else:
        gridA[guestrow][guestcol]="o"
        print("miss")
    player=0
    for row in gridA:
        player+=row.count("x")
    if player==3:
        print("player1 wins")
        break
    crow=random.randint(0,4)
    ccol=random.randint(0,4)
    if gridB[crow][ccol]=="^":
        gridB[crow][ccol]="x"
    else:
        gridB[crow][ccol]="o"
    computer=0
    for row in gridB:
        print("|".join(row))
        print("_________")
    for row in gridB:
        computer+=row.count("x")
    if computer==3:
        print("player2 wins")
        break