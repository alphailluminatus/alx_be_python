from bank_account import BankAccount

def main():
    # Create a bank account with optional starting balance
    account = BankAccount()

    while True:
        print("\n=== Bank Account Menu ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            account.display_balance()

        elif choice == "4":
            print("Goodbye! Thank you for using the Bank Account App.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 
4.")

if __name__ == "__main__":
    main()
