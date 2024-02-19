import random


mylist = ["Computer choses scissors","Computer choses Rock","Computer choses Paper"]
player = input("Rock Paper or Scissors \n")
puter = mylist
computer = random.choice(puter)
rock1 = player == ("rock")
paper1 = player == ("paper")
scissors1 = player == ("scissors")
computer_choose = random.choice(puter)
computer_output = str(computer)
computer_print = print(computer)
computer_think = str(computer_choose) + str(computer_output) + str(computer_print)
win_rock = str(computer) == ("Computer choses Scissors")
win_paper = str(computer) == ("Computer choses Rock")
win_scissors = str(computer) == ("Computer choses Paper") 
loose_rock = str(computer) == ("Computer choses Paper") 
loose_paper = str(computer) == ("Computer choses Scissors") 
loose_scissors = str(computer) == ("Computer choses Rock") 
winning = ("You Win :)")
loosing = ("You Loose :(")
drawing = ("Its a Draw :O")

#The Game

def main():
    if scissors1:
        computer_think
        if win_scissors:
            print (winning)
        elif loose_scissors: 
            print(loosing)
    
    elif rock1:
        computer_think
        if win_rock:
            print(winning)    
        elif loose_rock:
            print(loosing)
    
    elif paper1:
        computer_think
        if  win_paper:
            print (winning)
        elif loose_paper:
            print(loosing)
    
    else:
        print(drawing)

main()

