class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0

    def check_balance(self):
        print(f"Balance: {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit successful. Updated balance: {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated balance: {self._balance}")
        else:
            print("Balance is less. Withdraw not allowed")


class SavingsAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE = 0.04
        interest = self._balance * INTEREST_RATE
        print(f"Interest: {interest}")


class CurrentAccount(Account):
    def withdraw(self, amount):
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated balance: {self._balance}")
        else:
            print("Cash is over limit!")


class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._accounts = {}

    def create_account(self, id, holder_name, type):
        if type == "savings":
            new_account = SavingsAccount(id, holder_name)
        elif type == "current":
            new_account = CurrentAccount(id, holder_name)
        else:
            print("Invalid account type")
            return None

        self._accounts[id] = new_account
        print("Account creation successful")
        return new_account

    def get_account(self, id):
        if id not in self._accounts:
            print("Account not found")
            return None
        return self._accounts[id]


# TESTING
bk = Bank("Karnataka Bank", "Mysore")

s1 = bk.create_account("1", "Darshan", "savings")
c1 = bk.create_account("2", "Viral", "current")

s1.deposit(1000)
c1.deposit(100)

s1.withdraw(2000)
c1.withdraw(200)

s1.calculate_interest()

