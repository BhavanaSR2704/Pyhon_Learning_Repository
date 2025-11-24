# Wrapping data and functions into a single unit(object)

# Encapsulation:

# Create a BankAccount class with private attributes for account_number and balance.
# Add methods to check balance, deposit, and withdraw funds.
# accessing the balance directly and observe the result.


class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number #__is used for private
        self.__balance=balance
    def check_balance(self):
        print(self.__balance)
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance<amount:
            print("Insufficient funds")
            return
        self.__balance-=amount
        print(f"Withdraw successfull-Balance: {self.__balance}")
a=BankAccount(2704,100)
a.deposit(200)
a.check_balance()
