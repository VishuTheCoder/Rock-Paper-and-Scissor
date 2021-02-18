
# Rock, Paper and Scissors

# Started....(16 Feb 2021)

# Code as folow--------------------------------------------------------------------------------------------------------------------------------------------------------

import random

print("Let's play ROCK, PAPER AND SCISSORS. I think you know the rules so let's start")

User_Points = 0
Computer_Points = 0

User_Name = str(input("\nEnter your Name : "))

while True:

    Rock = 1
    Scissor = 3
    Paper = 2
    
    User_Move1 = str(input("1 = Rock\n2 = Paper\n3 = Scissor\nQ or q = Quit the Game\nPlay your move : "))

    if User_Move1 == "1":
        User_Move = 1
        print("Your move is ROCK")

    elif User_Move1 == "2":
        User_Move = 2
        print("Your move is PAPER")

    elif User_Move1 == "3":
        User_Move = 3
        print("Your move is SCISSOR")
        
    elif User_Move1 == "q" or User_Move1 == "Q":
        print("Computer's Score = " + str(Computer_Points) + "\n" + User_Name + " Score : " + str(User_Points))
        break
    
    else:
        print("Invalid Choice")
        continue
        
    Computer_Move = random.randint(Rock, Paper or Scissor)

    if Computer_Move == Rock:
        print("Computer's move is ROCK")

    elif Computer_Move == Paper:
        print("Computer's move is PAPER")

    elif Computer_Move == Scissor:
        print("Computer's move is SCISSOR")
    


    if Computer_Move == User_Move:
        print("It's a TIE")
        Computer_Points = Computer_Points + 0
        User_Points = User_Points + 0

    elif (Computer_Move == Rock and User_Move == Scissor) or (Computer_Move == Paper and User_Move == Rock) or (Computer_Move == Scissor and User_Move == Paper):
        print("\nComputer gets 1 POINT\n\n")
        Computer_Points = Computer_Points + 1
    else:
        print("\n" + User_Name + " gets 1 POINT")
        User_Points = User_Points + 1

    
    
        

    








