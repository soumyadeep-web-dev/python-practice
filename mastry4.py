#Python Number Guessing game
import random 
lowest_num=1
highest_num=100

guesses=0
actualNum= random.randint(lowest_num,lowest_num)
print("-------Python Number Guessing Game----------")

print(f"Select a number between {highest_num} and {highest_num}")

while True:
  
  guess= int(input("Enter your guess:  "))
  guesses+=1


  if(guess<1 or guess>100):
      print("The number is out of range!!!!!")

  elif(guess<actualNum):
      print("Too low! Try again!")
  elif(guess>actualNum):
      print("Too high! Try again")
  
  else:
    print("Correct Guess!!")
    print(f"The actual number was: {compNum}")
    print(f"Number of guesses: {guesses}")
    break


 