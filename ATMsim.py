class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self, account_type, pin):
        if self.verify_pin(pin):
            return f"Your {account_type} account balance is ${self.balance}"
        else:
            return "Incorrect PIN. Access denied."

    def deposit(self, amount, pin):
        if self.verify_pin(pin):
            self.balance += amount
            print(f"${amount} deposited successfully. Your new balance is ${self.balance}")
        else:
            print("Incorrect PIN. Access denied.")

    def withdraw(self, amount, pin):
        if self.verify_pin(pin):
            if amount <= self.balance:
                self.balance -= amount
                return f"${amount} withdrawn successfully. Your new balance is ${self.balance}"
            else:
                return "Insufficient funds"
        else:
            return "Incorrect PIN. Access denied."

    def mini_statement(self, pin):
        if self.verify_pin(pin):
            return f"Mini Statement: Your current balance is ${self.balance}"
        else:
            return "Incorrect PIN. Access denied."

    def verify_pin(self, pin):
        # For simplicity, a PIN is just a 4-digit number
        return str(pin).isdigit() and len(str(pin)) == 4


class ATM:
    def __init__(self):
        self.savings_account = Account()
        self.current_account = Account()

    def check_balance(self):
        print("Select Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        account_type = input("Enter your choice (1-2): ")

        if account_type == '1':
            pin = int(input("Enter your 4-digit PIN for Savings Account: "))
            print(self.savings_account.check_balance("Savings", pin))
        elif account_type == '2':
            pin = int(input("Enter your 4-digit PIN for Current Account: "))
            print(self.current_account.check_balance("Current", pin))
        else:
            print("Invalid choice. Please enter 1 or 2.")

    def deposit(self, account_type, amount, pin):
        if account_type == '1':
            self.savings_account.deposit(amount, pin)
        elif account_type == '2':
            self.current_account.deposit(amount, pin)
        else:
            print("Invalid account type")

    def withdraw(self, account_type, amount, pin):
        if account_type == '1':
            print(self.savings_account.withdraw(amount, pin))
        elif account_type == '2':
            print(self.current_account.withdraw(amount, pin))
        else:
            print("Invalid account type")

    def mini_statement(self, account_type, pin):
        if account_type == '1':
            print(self.savings_account.mini_statement(pin))
        elif account_type == '2':
            print(self.current_account.mini_statement(pin))
        else:
            print("Invalid account type")


def main():
    user_atm = ATM()

    while True:
        print("\nATM Simulator")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            user_atm.check_balance()
            break
        elif choice == '2':
            account_type = input("Enter the account type (1 for Savings, 2 for Current): ")
            amount = float(input("Enter the deposit amount: $"))
            pin = int(input("Enter your 4-digit PIN for your Account: "))
            user_atm.deposit(account_type, amount, pin)
            break
        elif choice == '3':
            account_type = input("Enter the account type (1 for Savings, 2 for Current): ")
            amount = float(input("Enter the withdrawal amount: $"))
            pin = int(input("Enter your 4-digit PIN for your Account: "))
            user_atm.withdraw(account_type, amount, pin)
            break
        elif choice == '4':
            account_type = input("Enter the account type (1 for Savings, 2 for Current): ")
            pin = int(input("Enter your 4-digit PIN for your Account: "))
            user_atm.mini_statement(account_type, pin)
            break
        elif choice == '5':
            print("Exiting ATM Simulator. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()