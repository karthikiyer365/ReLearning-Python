# "Rock, Paper, Scissors" Exercise
'''
Develop a Python application which will allow a human user to play a game of Rock-Paper-Scissors against a computer opponent. 
The game's functionality should adhere to the "Requirements" section below.
'''

### Determining the Winner
'''
The application should compare the user's selection to the computer player's selection, and determine which is the winner. The following logic should govern that determination:

  1. Rock beats Scissors
  2. Paper beats Rock
  3. Scissors beats Paper
  4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"
'''

import random as rn

def GamePlay(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return "It's a tie"
    elif playerChoice == 'rock':
        if computerChoice == 'paper':
            return "Computer wins! Game over"
        else:
            return "User won! Thanks for playing"
    elif playerChoice == 'paper':
        if computerChoice == 'scissors':
            return "Computer wins! Game over"
        else:
            return "User won! Thanks for playing"
    elif playerChoice == 'scissors':
        if computerChoice == 'rock':
            return "Computer wins! Game over"
        else:
            return "User won! Thanks for playing"


### Testing the Game
'''
In this function we are displaying how assert function of python can be used to ensure and test the game for possible runtime errors. 
By using test case scenarios in this assert function we can ensure that all edge cases are running smoothly'''

def GameTest():
    assert GamePlay(playerChoice = 'rock', computerChoice = "rock") == "It's a tie"
    assert GamePlay(playerChoice = 'paper', computerChoice = "paper") == "It's a tie"
    assert GamePlay(playerChoice = 'scissors', computerChoice = "scissors") == "It's a tie"
    assert GamePlay(playerChoice = 'rock', computerChoice = "paper") == "Computer wins! Game over"
    assert GamePlay(playerChoice = 'rock', computerChoice = "scissors") == "User won! Thanks for playing"
    assert GamePlay(playerChoice = 'paper', computerChoice = "scissors") == "Computer wins! Game over"
    assert GamePlay(playerChoice = 'paper', computerChoice = "rock") == "User won! Thanks for playing"
    assert GamePlay(playerChoice = 'scissors', computerChoice = "rock") == "Computer wins! Game over"
    assert GamePlay(playerChoice = 'scissors', computerChoice = "paper") == "User won! Thanks for playing"
    print("All cases passed")



### Displaying Results
'''
After determining the winner, the application should display the results to the user. Desired information outputs (from start to finish) includes the following:

  + A friendly welcome message, including the player's name (e.g. "Player One").
  + The user's selected option
  + The computer's selected option
  + Whether the user or the computer was the winner
  + A friendly farewell message
'''

name = str(input("Please input your player name: "))
print(" - - - - - - - - -")
replay = 'Y'
while(replay != 'N'):
    print("Welcome ",name," to my Rock-Paper-Scissors Game!")
    print(" - - - - - - - - -")
    options = ['rock', 'paper', 'scissors']
    playerChoice = str(input("Please Choose an option ['rock', 'paper', 'scissors']: " )).lower()
    print(" - - - - - - - - -")
    computerChoice = rn.choice(options)
    while playerChoice not in options:
        playerChoice = str(input("Invalid Input. Try again: ")).lower()
        print(" - - - - - - - - -")
    result = GamePlay(playerChoice, computerChoice)
    print("User Choice:", playerChoice)
    print(" - - - - - - - - -")
    print("Computer Choice:", computerChoice)
    print(" - - - - - - - - -")
    print(result)
    print(" - - - - - - - - -")
    replay = str(input("Do you want to replay(Y/N)? ").upper())
    print("- - - - - - - - -")


tester = input("Do you wish to test all cases?(Y/N)")
if(tester.upper() == 'Y'):
    GameTest()

