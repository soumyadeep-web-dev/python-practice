import random

print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │ "
"│         │ "
"│         │ "
"└─────────┘"

dice_art={ 1:("┌─────────┐",
              "│         │ ",
              "│    ●    │ ",
              "│         │ ",
              "└─────────┘"),
           2:("┌─────────┐",
              "│  ●      │ ",
              "│         │ ",
              "│      ●  │ ",
              "└─────────┘"),
           3:("┌─────────┐",
              "│ ●       │ ",
              "│    ●    │ ",
              "│       ● │ ",
              "└─────────┘"),
           4:("┌─────────┐",
              "│ ●     ● │ ",
              "│         │ ",
              "│ ●     ● │ ",
              "└─────────┘"),
           5:("┌─────────┐",
              "│ ●     ● │ ",
              "│    ●    │ ",
              "│ ●     ● │ ",
              "└─────────┘"),
           6:("┌─────────┐",
              "│ ●     ● │ ",
              "│ ●     ● │ ",
              "│ ●     ● │ ",
              "└─────────┘"), }

dice=[]
total=0
no_of_dice=int(input("Enter the number of times the die to be rolled:  "))

for die in range(no_of_dice):
   dice.append(random.randint(1,6))

for num in dice:
   for lines in dice_art.get(num):
      print(lines)  

for count in dice:
   total+=count
print(total)