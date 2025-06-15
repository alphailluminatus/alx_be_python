from bank_account import BankAccount

def main():
    account = BankAccount(250)
    account.deposit(67)
    account.withdraw(50)
    account.withdraw(300)
    account.display_balance()

if __name__ == "__main__":
    main()

