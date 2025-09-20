import random
words=["mine","your","me","outlander","not","photon","accelerator","extractor","ok"]
stages=[
    '''
      |
      ''',
      '''
      |
      O
      ''',
      '''
      |
      O
      |
      ''',
      '''
      |
      O
     /|
      ''',
      '''
      |
      O
     /|\\
      ''',
      '''
      |
      O
     /|\\
     / 
      ''',
    '''
      |
      O
     /|\\
     / \\
      ''']

while True:
    counter=0
    word=random.choice(words)
    list=["_"]*len(word)
    print(list)

    while True:
        hang=" ".join(list)
        print(hang)
        letter=input("guess a letter?")
        if letter in word:
            for i in range(len(word)):
                if letter==word[i]:
                    list[i]=letter
        else:
            print(stages[counter])
            counter=counter+1
            if counter==7:
                break
        if "".join(list)==word:
            print("correct")
            break
    them=input("do you want to play again")
    if them=="yes":
        print("ok:)")
    elif them=="no":
        print("ok:(")
        break