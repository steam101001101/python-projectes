grid=[ 
      [" ", " ", " "],
      [" ", " ", " "],
      [" ", " ", " "]
]
for row in grid:
    print("|".join(row))
    print("-----")
player="X"
stop=True
while stop:
    print("Player",player)
    row=int(input("which row?"))
    col=int(input("which column?"))
    if grid[row][col]==" ":
        grid[row][col]=player
    else:
        print("try again")
        continue
    for row in grid:
        print("|".join(row))
        print("-----")
    if grid[0][0]==grid[0][1] and grid[0][1]==grid[0][2] and grid[0][1]!=" ":
        print("Player wins",player)
        stop=False
    if grid[1][0]==grid[1][1] and grid[1][1]==grid[1][2] and grid[1][1]!=" ":
        print("Player wins",player)
        stop=False
    if grid[2][0]==grid[2][1] and grid[2][1]==grid[2][2] and grid[2][1]!=" ":
        print("Player wins",player)
        stop=False
    if grid[0][1]==grid[1][1] and grid[1][1]==grid[2][1] and grid[0][1]!=" ":
        print("Player wins",player)
        stop=False
    if grid[0][0]==grid[1][0] and grid[1][0]==grid[2][0] and grid[1][0]!=" ":
        print("Player wins",player)
        stop=False
    if grid[0][2]==grid[1][2] and grid[1][2]==grid[2][2] and grid[1][2]!=" ":
        print("Player wins",player)
        stop=False
    if grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2] and grid[1][1]!=" ":
        print("Player wins",player)
        stop=False
    if grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0] and grid[1][1]!=" ":
        print("Player wins",player)
        stop=False
    if player=="X":
        player="o"
    elif player=="o":
        player="X"