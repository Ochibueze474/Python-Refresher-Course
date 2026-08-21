# Python Banking Program

def show_balance(balance):
    print()
    print(f"Your balance is #{balance:.2f}")

def deposit():
    print()
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    print()
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds!")
        return 0
    elif amount < 0:
        print("The amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True


    while is_running:
        print()
        print("Banking Program")
        print("1.Show balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Exit")
        print()

        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank You! Have a nice day")

if __name__ == "__main__":
    main()
