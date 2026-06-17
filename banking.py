
def show_balance(balance):
  print(f"Your balance is Rs{balance}")

def deposit(balance,dep_amt):
  balance+=dep_amt
  return balance

def withdraw(balance,amount):
  balance-=amount
  return balance
  

def main():

  balance=0
  is_running=True
  print("****************************")
  print("Welcome to the People's Bank")
  print("****************************")

  while is_running:
    print("Baking Operations:")
    print("1.Show balance")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Exit")
    choice=int(input("Please enter your choice(1 to 4): "))

    match choice:
      case 1:
        show_balance(balance)
      case 2:
        amount=int(input("Please enter the amount you want to withdraw: "))
        if amount>balance:
          print("Insufficient balace!")
        else:
          balance=withdraw(balance,amount)
      case 3:
        dep_amt=int(input("Please enter the amount you want to deposit: "))
        balance=deposit(balance,dep_amt)
      case 4:
        is_running=False










  

if __name__=="__main__":
  main()