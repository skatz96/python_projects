#we are importing this library
from random import randint



def convertNumToMove(move):
  if (move == 1):
    return "rock"
  elif (move == 2):
    return "scissors"
  elif (move == 3):
    return "paper"
    
    
# define function
def decideWinner(playerMove, compMove):
  if (playerMove == "rock" and compMove == 1):
    print("Tie!")
  elif (playerMove == "rock" and compMove == 2):
    print("rock beats scissors! Player wins!")
  elif (playerMove == "rock" and compMove == 3):
    print("paper beats rock! Comp wins!")
  elif (playerMove == "scissors" and compMove == 2):
    print("Tie!")
  elif (playerMove == "scissors" and compMove == 1):
    print("Rock beats scissors! Comp wins!")
  elif (playerMove == "scissors" and compMove == 3):
    print("Scissors beats paper! Player wins!")
  elif (playerMove == "paper" and compMove == 3):
    print("Tie!")
  elif (playerMove == "paper" and compMove == 2):
    print("Scissors beats paper! Player wins!")
  elif (playerMove == "paper" and compMove == 1):
    print("Paper beats rock! Player wins!")
    
    
# start the game
print("What is your move?")
playerMove = input()
print("You threw a",playerMove,"!")

print("Computer is making a move now...")
compMove = randint(1,3)
print("Computer threw a", convertNumToMove(compMove))
decideWinner(playerMove, compMove)
