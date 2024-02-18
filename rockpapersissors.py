import random

#Defintions  
mylist = ["Computer choses Sissors","Computer choses Rock","Computer choses Paper"]
player = input("Rock Paper or Sissors \n")
puter = mylist
computer = random.choice(puter)

rock = player == ("rock")
paper = player == ("paper")
sissors = player == ("sissors")

computer_choose = random.choice(puter)
computer_output = str(computer)
computer_print = print(computer)

win_rock = str(computer) == ("Computer choses Sissors")
win_paper = str(computer) == ("Computer choses Rock")
win_sissors = str(computer) == ("Computer choses Paper") 

loose_rock = str(computer) == ("Computer choses Paper") 
loose_paper = str(computer) == ("Computer choses Sissors") 
loose_sissors = str(computer) == ("Computer choses Rock") 

winning = ("You Win :)")
loosing = ("You Loose :(")
drawing = ("Its a Draw :O")

##########The game
if sissors:
    computer_choose
    computer_output
    computer_print
    if win_sissors:
        print (winning)
    elif loose_sissors: 
        print(loosing)
    else:
        print(drawing)
    
    

elif rock:
    computer_choose
    computer_output
    computer_print
    if win_rock:
        print (winning)    
    elif loose_rock:
        print(loosing)
    else: 
        print(drawing)


elif paper:
    computer_choose
    computer_output
    computer_print
    if win_paper:
        print (winning)
    elif loose_paper:
        print(loosing)
    else:
        print(drawing)

    
    




