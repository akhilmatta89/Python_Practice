"""
Encapsulation means wrapping data (variables) and methods (functions) together,
restricting direct access to internal data from outside the class.

To protect data and control modification through controlled access (getters/setters).

Python does not enforce access restrictions strictly like Java or C++, but uses:

    * _variable → Protected (by convention)
    * __variable → Private (name mangled)

"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__protected_withdraw(amount)

    def __protected_withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Akhil", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())         # ✅ OK

# print(acc.__balance)          # ❌ Error: private variable
print(acc._BankAccount__balance) # ⚠️ Name mangling access (not recommended)
