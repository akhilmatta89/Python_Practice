"""
Practice Task 9: Hierarchical Inheritance
Create a base class Account with method:

account_type() → "This is a bank account"

Create two derived classes:

SavingsAccount with method: interest_rate() → "Interest rate is 4%"

CurrentAccount with method: overdraft_limit() → "Overdraft limit is ₹50,000"

Create objects of both subclasses and call their own and parent methods.

"""

class Account:

    def account_type(self):
        print("This is a bank account")

class SavingsAccount(Account):
    def interest_rate(self):
        print("Interest rate is 4%")

class CurrentAccount(Account):
    def overdraft_limit(self):
        print("Overdraft limit is ₹50,000")

s = SavingsAccount()
s.account_type()
s.interest_rate()

c = CurrentAccount()
c.account_type()
c.overdraft_limit()