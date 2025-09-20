import random
words=["put","four","time","scramble","mine","six","move","rebel","vulture"]
while True:
    word=random.choice(words)
    thelist=list(word)
    random.shuffle(thelist)
    scramble_word="".join(thelist)
    print(scramble_word)
    for i in range(5):
        you=input("guess the word ")
        if you==word:
            print("corret")
            break
        else:
            print("wrong")
    them=input("do you want to play again")
    if them=="yes":
        print("continue")
    elif them=="no":
        break