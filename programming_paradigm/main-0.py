from bank_account import BankAccount

def main():
    account = BankAccount()
    account.deposit(67)        # Will print: Deposited: $67.0
    account.withdraw(50)       # Will print: Withdrew: $50.0
    account.withdraw(100)      # Will print: Insufficient funds.
    account.display_balance()  # Will print: Current Balance: $17.00

if __name__ == "__main__":
    main()

