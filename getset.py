class BankAccount:
    def __init__(self, account_number, account_holder, pin, initial_balance=0):
        # Public attributes
        self.account_number = account_number
        self.account_holder = account_holder
        # Private attributes
        self.__balance = initial_balance
        self.__pin = pin

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    # Method to withdraw money
    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount > 0:
                if amount <= self.__balance:
                    self.__balance -= amount
                    print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.__balance:.2f}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be greater than zero.")
        else:
            print("Incorrect PIN. Withdrawal denied.")

    # Method to check the balance (optional)
    def check_balance(self, pin):
        if pin == self.__pin:
            print(f"Current balance: ${self.__balance:.2f}")
        else:
            print("Incorrect PIN. Cannot access balance.")

# Example usage
account = BankAccount(account_number="45947", account_holder="Emily", pin=666329, initial_balance=100)
account.deposit(50)
account.withdraw(30, pin=666329)
account.withdraw(200, pin=666329)  # Should indicate insufficient funds
account.check_balance(pin=666329)
account.withdraw(20, pin=923666)  # Should deny due to incorrect PIN