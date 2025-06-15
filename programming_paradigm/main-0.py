from bank_account import BankAccount

def main():
    account = BankAccount()
    account.deposit(67.0)
    account.withdraw(50.0)
    account.withdraw(100.0)
    account.display_balance()

if __name__ == "__main__":
    main()
