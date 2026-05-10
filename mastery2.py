questions=("what's the largest planet",
"what's the lightest elemet?",
 "Biggest Animal?",
  "Largest river?",
   "Smallest country?",                                        )

options=(("A.Mercury","B.Mars","C.Jupiter","D.Uranus"),
         ("A.Hydragen","B.Copper","C.helium","D.xenon"),
         ("A.Ostritch","B.eleplant","C.blue whale","D.Shark"),
         ("A.Ganga","B.Nile","C.Amazon","D.Tigris"),
         ("A.Vatican","B.Bhutan","C.Iceland","D.Japan"))

answers=("C","A","C","C","A")

guesses=[]
score=0
question_num=0

print("--------Start-----------")

for question in questions:
  print("--------------------------------")
  print(question)
  for option in options[question_num]:
    print(option)
  answer=input("You're answer:  ").upper()
  guesses.append(answer)
  if answer== answers[question_num]:
    score+=1
    print("You're answer is correct")
  else:
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")  
  question_num+=1
print("---------End----------")

print(f"You're answers are:")
for x in guesses:
  print(x,end=" ")
print()

print(f"Correct answers are:")
for x in answers:
  print(x,end=" ")
print()

percen= int(score/len(questions)*100)
print(f"You're final score: {percen}") 
    
