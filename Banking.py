def show_balance(balance):
    print(f"your balance is {balance:.2f} rupees")

def deposit():
    amount=int(input("Enter a amount to deposit : "))
    if amount<0:
        print("!Invalid Amount")
        return 0
    else:
        return amount
        
def withdraw(balance):
    amount=float(input("Enter a amount to withdraw : "))
    if amount > balance:
        print("Insufficent Amount")
        return 0
    elif amount<0:
        print("!Invalid Amount")
        return 0
    else:
        return amount
def main():
        
    balance = 0
    is_running=True
    
    
    while is_running:
        print("****************")
        print("Banking Program")
        print("****************")
        print()
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.Exit")
        print()
        choice = input("Enter your choice (1-4) : ")
            
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance+=deposit()
        elif choice == "3":
            balance-=withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid!")

    print("Thank You! Have a nice day")

if __name__=="__main__":
    main()
    
        