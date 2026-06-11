"""
- Abstract Factory provides an interface to create families of related objects without
    specifying their concrete classes.

- Abstract Factory creates multiple related objects that are meant to work together.

- Use Abstract Factory when:
    - You need to create groups of related objects
    - You want to switch entire “families” easily
    - You want to avoid hardcoding object creation everywhere

- Imagine a banking system that supports different Banking Platforms:
    Platform 1: Retail Banking
        Retail Loan Processor
        Retail Payment Processor
        Retail Account Validator

    Platform 2: Corporate Banking
        Corporate Loan Processor
        Corporate Payment Processor
        Corporate Account Validator

    Platform 3: FinTech Banking
        FinTech Loan Processor
        FinTech Payment Processor
        FinTech Account Validator

when Each platform needs a set of related objects.Abstract Factory lets you create these families cleanly.

                                Abstract Product Interfaces
                                Concrete Product Families

                                Abstract Factory Interface
                                Concrete Factories (Families)

                                Client Code (Super Clean)
"""

# STEP-1: we create abstract product interfaces
from abc import ABC, abstractmethod

class LoanProcessor(ABC):
    @abstractmethod
    def process_loan(self, loan_amount):
        pass

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class AccountValidator(ABC):
    @abstractmethod
    def validate(self,account_id):
        pass

# STEP-2: We Create Concrete Product Families
class RetailLoanProcessor(LoanProcessor):
    def process_loan(self,loan_amount):
        if loan_amount <= 0:
            print("Loan amount must be greater than 0")
        else:
            print(f"Processing Retail Loan Amount of {loan_amount} euros")

class RetailPaymentProcessor(PaymentProcessor):
    def pay(self,amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        else:
            print(f"Paying the Retail Payment Amount of {amount} euros")

class RetailAccountValidator(AccountValidator):
    def validate(self,account_id):
        print(f"Validating Retail Account {account_id}")


class CorporateLoanProcessor(LoanProcessor):
    def process_loan(self,loan_amount):
        if loan_amount <= 0:
            print("Loan amount must be greater than 0")
        else:
            print(f"Processing Corporate Loan Amount of {loan_amount} euros")

class CorporatePaymentProcessor(PaymentProcessor):
    def pay(self,amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        else:
            print(f"Paying the Corporate Payment Amount of {amount} euros")

class CorporateAccountValidator(AccountValidator):
    def validate(self,account_id):
        print(f"Validating Corporate Account {account_id}")


class FintechLoanProcessor(LoanProcessor):
    def process_loan(self,loan_amount):
        if loan_amount <= 0:
            print("Loan amount must be greater than 0")
        else:
            print(f"Processing Fintech Loan Amount of {loan_amount} euros")

class FintechPaymentProcessor(PaymentProcessor):
    def pay(self,amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        else:
            print(f"Paying the Fintech Payment Amount of {amount} euros")

class FintechAccountValidator(AccountValidator):
    def validate(self,account_id):
        print(f"Validating Fintech Account {account_id}")


# STEP-3: we create the abstract factory interface

class BankingFactory(ABC):
    @abstractmethod
    def create_loan_processor(self):
        pass
    @abstractmethod
    def create_payment_processor(self):
        pass
    @abstractmethod
    def create_account_validator(self):
        pass

# STEP-4: we create concrete factories of families
class RetailBankingFactory(BankingFactory):
    def create_loan_processor(self):
        return RetailLoanProcessor()
    def create_payment_processor(self):
        return RetailPaymentProcessor()
    def create_account_validator(self):
        return RetailAccountValidator()

class CorporateBankingFactory(BankingFactory):
    def create_loan_processor(self):
        return CorporateLoanProcessor()
    def create_payment_processor(self):
        return CorporatePaymentProcessor()
    def create_account_validator(self):
        return CorporateAccountValidator()

class FintechBankingFactory(BankingFactory):
    def create_loan_processor(self):
        return FintechLoanProcessor()
    def create_payment_processor(self):
        return FintechPaymentProcessor()
    def create_account_validator(self):
        return FintechAccountValidator()