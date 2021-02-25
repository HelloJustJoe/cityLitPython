import random

def userMove():
    choice = input("Get ready! Choose rock, paper or scissors! R / P / S : " ).lower()
    while (choice != "r") and (choice != "p") and (choice != "s"):
        choice = input("Huh? Sorry, please type R for rock, P for paper or S for scissors! : ").lower()
    return choice

def compMove():
    if random.randint(1,3) == 1:
        return "r"
    elif random.randint(1,3) == 2:
        return "p"
    else:
        return "s"

def round():
    p1 = userMove()
    p2 = compMove()
    if (p1 == "r" and p2 == "p") or (p1 == "p" and p2 == "s") or (p1 == "s" and p2 == "r"):
        return "Computer Victory"
    elif (p1 == "r" and p2 == "s") or (p1 == "p" and p2 == "r") or (p1 == "s" and p2 == "p"):
        return "Player Victory"
    else:
        return "Draw"

def rematch():
    playAgain = input("Would you like to play again? Y / N : ").lower()
    while (playAgain != "y") and (playAgain != "n"):
        playAgain = input("Huh? Sorry, please type Y or N : ").lower()
    if playAgain == "y": 
        round()
    else: 
        exit() 

def game():
    print(round())
    rematch()


print (game())
