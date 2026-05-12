# Concession stand program 

menu={"POPCORN":1.00,
          "HOT DOG":2.00,
          "GIANT PRETZEL":2.00,
          "ASST CANDY":1.00,
          "SODA":1.00,
          "BOTTLED WATER":1.00}

# capitals.keys()
# print(capitals.items())
order=[]
total=0

for item,value in menu.items():
  print(f"{item}:${value:.2f}")
 

while True:
  item=input("What would to like to have(q to quit):").upper()
  if item== "Q":
    break
  elif menu.get(item) is not None:
    order.append(item)
    cost = menu.get(item)
    print(f"The price: ${cost:.2f}")
    total+=cost
print("---------Checkout----------")  
for item in order:
  print(f"{item}:     ${menu.get(item)}") 
print(f"             -${total}")   

  
