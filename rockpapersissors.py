import random
import turtle

 
#game  
mylist = ["Computer choses Sissors","Computer choses Rock","Computer choses Paper"]

player = input("Rock Paper or Sissors \n")

puter = mylist
 
computer = random.choice(puter)

win_rock = str(computer) == ("Computer choses Sissors")
win_paper = str(computer) == ("Computer choses Rock")
win_sissors = str(computer) == ("Computer choses Paper") 

loose_rock = str(computer) == ("Computer choses Paper") 
loose_paper = str(computer) == ("Computer choses Sissors") 
loose_sissors = str(computer) == ("Computer choses Rock") 

winning = ("You Win")

##########The game
if player == ("sissors"):
    random.choice(puter)
    str(computer)
    print(computer)
    if win_sissors:
        print (winning)
    elif loose_sissors: 
        print("Try again")
    else:
        print("Draw")
    
    

elif player == ("rock"):
    random.choice(puter)
    str(computer)
    print(computer)
    if win_rock:
        print (winning)    
    elif loose_rock:
        print("Try Again")
    else: 
        print("Draw")


elif player == ("paper"):
    random.choice(puter)
    str(computer)
    print(computer)
    if win_paper:
        print (winning)
    elif loose_paper:
        print("Try Again")
    else:
        print("Draw")

    
    




