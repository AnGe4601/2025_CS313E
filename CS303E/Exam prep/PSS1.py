import math 

r, h = eval(input("Enter a value for r and h:") )
volume = math.pi * r * r * h
print(volume)



import random as r
 
user = input("Choose rock, paper, or scissors: ")
    
computer =  r.randint(0, 2)

if user == "rock":
    user = 0
    if computer == 0:
        computer = "rock"
        user = "rock"
        print(f"Computer is {computer}. You are {user}.\nDraw.")
    elif computer == 1:
        computer = "paper"
        user = "rock"
        print(f"Computer is {computer}. You are {user}.\nComputer wins.")
    else:
        computer = "scissors"
        user = "rock"
        print(f"Computer is {computer}. You are {user}.\nYou win.")
elif user == "paper":
    user = 1
    if computer == 0:
        computer = "rock"
        user = "paper"
        print(f"Computer is {computer}. You are {user}.\nYou win.")
    elif computer == 1:
        computer = "paper"
        user = "paper"
        print(f"Computer is {computer}. You are {user}.\nDraw.")
    else:
        computer = "scissors"
        user = "paper"
        print(f"Computer is {computer}. You are {user}.\nComputer wins.")
else:
    user = 2
    if computer == 0:
        computer = "rock"
        user = "scissors"
        print(f"Computer is {computer}. You are {user}.\nComputer wins.")
    elif computer == 1:
        computer = "paper"
        user = "scissors"
        print(f"Computer is {computer}. You are {user}.\nYou win.")
    else:
        computer = "scissors"
        user = "scissors"
        print(f"Computer is {computer}. You are {user}.\nDraw.")
'''
