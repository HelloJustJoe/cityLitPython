import random

moves = ["rock", "paper", "scissors"]


def userMove():
    choice = input("\nGet ready! Choose rock, paper or scissors! \nrock / paper / scissors : ").lower()
    while (choice not in moves):
        choice = input("\nHuh? Sorry, please type rock, paper or scissors! \nrock / paper / scissors : ").lower()
    return choice
    

def compMove():
    return random.choice(moves)


def bestOf():
    number = input("Best of...? : ")
    while (number.isnumeric() == False): 
        number = input("Huh?! Sorry please enter a number! Positive integers only! : ")
    return int(number)


def rematch():
    playAgain = input("Would you like to play again? \nY / N : ").lower()
    while (playAgain != "y") and (playAgain != "n"):
        playAgain = input("Huh? Sorry, please type Y or N \nY / N : ").lower()
    if playAgain == "y": 
        games = bestOf()
        rockPaperScissorsGame(games)
    else: 
        exit() 


def rockPaperScissorsGame(num = 3, userScore = 0, compScore = 0):
    while (num > 0):
        userTurn = userMove()
        compTurn = compMove()
        print(f"PLAYER = {userTurn}, COMPUTER = {compTurn}")
        if (userTurn == "rock" and compTurn == "paper") or (userTurn == "paper" and compTurn == "scissors") or (userTurn == "scissors" and compTurn == "rock"):
            compScore += 1
            print(f"\nYou lost this round! Your opponent chose {compTurn} while you had {userTurn}!\n")
            print(f"Player Score : {userScore}\nComputer Score : {compScore}")
            num -= 1
        elif (userTurn == "rock" and compTurn == "scissors") or (userTurn == "paper" and compTurn == "rock") or (userTurn == "scissors" and compTurn == "paper"):
            userScore += 1
            print(f"\nYou won this round! Your opponent chose {compTurn} while you had {userTurn}!\n")
            print(f"Player Score : {userScore}\nComputer Score : {compScore}")
            num -= 1
        else:
            print(f"\nAh! You both chose {userTurn}!\n")
            print(f"Player Score : {userScore}\nComputer Score : {compScore}")

    if (userScore > compScore): print(f"Congratulations! You won!")
    if (compScore > userScore): print(f"Oh no! You lost!")
    if (compScore == userScore): print(f"Draw! What a close game!")
    
    rematch()


games = bestOf()
rockPaperScissorsGame(games)


# Very Hard: Who wins rock-paper-scissors is random if the two players choose
# randomly. But humans are bad at doing that; we tend to follow unconscious
# patterns. Adapt your rock-paper-scissors game to exploit this. Have the computer
# remember the sequence of moves you played in multiple games and use it to predict
# what your next move might be. For example, if you win a turn, are you more likely to
# pick the same again on your next turn? Test your programme on someone else and
# see if it can beat them more than 50% of the time.