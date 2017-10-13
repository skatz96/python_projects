
playAgain = "yes"

while (playAgain == "yes"):
  
  score = 0
  
  print(" Is Sadie a senior? (yes/no)")
  answer = input()
  
  if (answer == "yes"):
    score = score + 1
    print("Correct!")
  else:
    print("Incorrect")
  
  
  print("How many semesters does Sadie have left?")
  answer = input()
  
  if (answer == "2"):
    score = score + 1
    print("Correct!)")
  else:
    print("Incorrect")
  
    
  
  print("How many hours of sleep does Sadie need each night?")
  answer=input()
  
  if (answer == "8"):
    score = score + 1
    print ("Correct!")
  else: 
    print ("Incorrect")
    
  
  print ("If I have five apples, and I give my friend Samantha two apples, how many apples do I have left?")
  answer= input()
  
  if (answer == "3"):  
    score = score + 1
    print ("Correct!")
  else:
    print ("Incorrect")
    
  
  print ("How many meals are there in a day? ")
  answer=input()
    
  if (answer == "3"):
    score = score + 1
    print ("Correct!")
  elif (answer == "2"):
    print ("Wrong!!!")
  else:
    print ("Wrong!!!")
    
  
  print ("How many kids does Sadie want to have?")
  answer= input()
  
  if (int(answer) > 3):
    score= score + 1
    print("Wrong!")
  elif (int(answer) < 3):
    print("Correct!")
  
  print("Do you want to play again?")
  playAgain = input()
  
  
  
  
  
  
  
  