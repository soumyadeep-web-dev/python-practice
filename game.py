#Rock-paper_scissor game
import random


options=("rock","paper","scissors")

playing= True

while playing:

    computer= random.choice(options)
    player= None

    while player not in options:
      player=input("Enter you're move(rock,paper,scissor):  ")
      if player==computer:
        print(f"Computer: {computer}")
        print(f"You're Move: {player}")
        print("Tie!!!")
      elif player == "rock" and computer=="scissors":
        print(f"Computer: {computer}")
        print(f"You're Move: {player}")
        print("You Win!!!")
      elif player=="scissors" and computer=="paper":
        print(f"Computer: {computer}")
        print(f"You're Move: {player}")
        print("You Win!!!") 
      elif player=="paper"and computer=="rock":
        print(f"Computer: {computer}")
        print(f"You're Move: {player}")
        print("You win!!!")
      else:
        print(f"Computer: {computer}")
        print(f"You're Move: {player}")
        print("You Loose!!!")
      
      if not input("Play again?(y/n)")=="y":
        playing=False
print("Thank You for playing")       
        

