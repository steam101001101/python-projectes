import random
grid=[["_","_","_","_"],["_","_","_","_"],["_","_","_","_"],["_","_","_","_"]]
print(grid)
for row in grid:
    for i in row:
        print(i,end=" ")
    print()
trow=random.randint(0,3)
tcol=random.randint(0,3)
for i in range(3):
    number_row=int(input("what row?"))
    number_col=int(input("what col?"))
    if number_row<trow:
        print("move down")
    elif number_row>trow:
        print("move up")
    if number_col>tcol:
        print("move left")
    elif number_col<tcol:
        print("move right")
    if number_row==trow and number_col==tcol:
        print("correct")
        break
    else:
        print("incorrect")