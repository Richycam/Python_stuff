import random

##########Listing my varibles 
mylist = ["Sissors","Rock","Paper"]

player = input("Rock Paper or Sissors \n")

puter = mylist
 
computer = random.choice(puter)

win_rock = player == ("rock") + computer == ("Sissors")
win_paper = player == ("paper") + computer == ("Rock")
win_sissors = player == ("sissors") + computer == ("Paper")

##########The game
if player == str("sissors"):
    random.choice(puter)
    str(computer)
    print(computer)
    if win_sissors:
        print ("You win")
    else:
        print("You loose")
    
    

elif player == str("rock"):
    random.choice(puter)
    str(computer)
    print(computer)
    if win_rock:
        print ("You win")
    else:
        print("You loose")
    


elif player == str("paper"):
    random.choice(puter)
    str(computer)
    print(computer)
    if win_paper:
        print ("You win")
    else:
        print("You loose")
    

    
    




