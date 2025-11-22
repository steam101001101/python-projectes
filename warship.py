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
print(gridA)
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