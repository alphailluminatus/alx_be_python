from bank_account import BankAccount

def main():
    account = BankAccount()
    account.deposit(67)            # Prints once from inside the method
    account.withdraw(50)           # Also prints from method
    account.withdraw(100)          # Also prints from method
    account.display_balance()      # Prints balance

if __name__ == "__main__":
    main()

