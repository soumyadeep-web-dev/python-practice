foods=[]
prices=[]
total= 0

while True:
   item=input("What you want to buy(q to quite): ")
   if item == "q":
      break
   else:
      cost=int(input("What's the peice: "))
      foods.append(item)
      prices.append(cost)

print("------You're Cart---------")
for food in foods:
   print(food, end=" ")

for price in prices:
   total+=price
print(f"Total prices is Rs{total}")   
     
