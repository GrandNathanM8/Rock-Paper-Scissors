# Dependencies
import random, time, emoji
from termcolor import colored
# -










# Functions
Choices = ["Rock", "Paper", "Scissors"]





def GET_USER_CHOICE():
    while True:
        Input = input("Enter your choice (Rock, Paper, or Scissors): ").title()
        if Input in Choices:
            return Input
        else:
            print("Invalid choice. Please try again.")
            
            
def GET_COMPUTER_CHOICE():
    return random.choice(Choices)


def RESOLVE(USER, COMPUTER):
    Outcomes = {
        "Rock": {"Rock": "tie", "Paper": "Lose", "Scissors": "Won"},
        "Paper": {"Rock": "win", "Paper": "Tie", "Scissors": "Lose"},
        "scissors": {"Rock": "lOSE", "Paper": "Won", "Scissors": "Tie"}
    }
    return Outcomes[USER][COMPUTER]


def DISPLAY_CHOICE(USER, COMPUTER):
    print(f"\nYou chose: {colored(USER, 'cyan')}")
    print(f"Computer chose: {colored(COMPUTER, 'cyan')}")
    
    
def DISPLAY_RESULT(Result):
    if Result == "Tie":
        print(colored(emoji.emojize("It's a tie! :handshake:"), "yellow"))
    elif Result == "Won":
        print(colored(emoji.emojize("You won! :trophy:"), "green"))
    else:
        print(colored(emoji.emojize("Computer WON! \U0001F916"), "red"))
        
        
def PLAY_GAME():
    print("\n\033[1mLet's play Rock-Paper-Scissors!\033[0m")
    while True:
        UC = GET_USER_CHOICE()
        CC = GET_COMPUTER_CHOICE()

        print("\n\033[1mRock...\033[0m")
        time.sleep(1)
        print("\033[1mPaper...\033[0m")
        time.sleep(1)
        print("\033[1mScissors...\033[0m")
        time.sleep(1)

        DISPLAY_CHOICE(UC, CC)
        
        Result = RESOLVE(UC, CC)
        DISPLAY_RESULT(Result)

        Prompt = input("\nDo you want to play again? (Yes/No): ").title()
        if Prompt != "Yes":
            break
# -















# Execution
Execute = PLAY_GAME()
