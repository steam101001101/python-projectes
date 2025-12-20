products={"laptop":315,"table":25,"tv":1502,"chess_board":14,"tennis_racket":41,"shampoo":30,"phone":261,"ps5":1050,"xbox console":502}
for key,value in products.items():
    print(key,"£"+str(value))
cart={}
while True:
    buyer=input("what product are you buying? type no if not")
    if buyer=="no":
        break
    if buyer not in products:
        print("this product is not availble")
        continue
    quantity=int(input("how many are you buying?"))
    cart[buyer]=quantity
    print(cart)
total_cost=0
for key,value in cart.items():
    amount=value*products[key]
    print(key,value,products[key],amount)
    total_cost+=amount
print("This is the final amount",total_cost)