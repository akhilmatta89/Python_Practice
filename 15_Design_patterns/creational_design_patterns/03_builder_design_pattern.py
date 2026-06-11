"""
Builder Pattern lets you construct complex objects step‑by‑step,
allowing different representations using the same construction process.

Imagine a bank onboarding system.
    A Customer Profile is complex and may include:
        Personal details
        KYC verification
        Credit score
        Account type
        Optional services (loan eligibility, debit card, insurance, etc.)

Different customer types require different setups:
    Retail Customer
    Corporate Customer

The Builder Pattern lets you build these profiles step‑by‑step, but with different builders.

"""
# STEP-1: This is the product(complex object)
class CustomerProfile:
    def __init__(self):
        self.name = None
        self.kyc_verification = False
        self.credit_score = None
        self.account_type = None
        self.optional_services = []

    def __str__(self):
        return str(self.__dict__)

# STEP-2: We create the builder interface
from abc import ABC, abstractmethod

class CustomerBuilder(ABC):
    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def verify_kyc(self):
        pass

    @abstractmethod
    def set_credit_score(self, credit_score):
        pass

    @abstractmethod
    def set_account_type(self):
        pass

    @abstractmethod
    def set_optional_services(self):
        pass

    @abstractmethod
    def build(self):
        pass

# STEP-3: we create the concrete builders
class RetailCustomerBuilder(CustomerBuilder):

    def __init__(self):
        self.profile = CustomerProfile()

    def set_name(self, name):
        self.profile.name = name

    def verify_kyc(self):
        self.profile.kyc_verification = True

    def set_credit_score(self, credit_score):
        self.profile.credit_score = credit_score

    def set_account_type(self):
        self.profile.account_type = "Retail Savings Account"

    def set_optional_services(self):
        self.profile.optional_services.append("Debit Card")
        self.profile.optional_services.append("Mobile Banking")

    def build(self):
        return self.profile

class CorporateCustomerBuilder(CustomerBuilder):

    def __init__(self):
        self.profile = CustomerProfile()

    def set_name(self, name):
        self.profile.name = name

    def verify_kyc(self):
        self.profile.kyc_verification = True

    def set_credit_score(self, credit_score):
        self.profile.credit_score = credit_score

    def set_account_type(self):
        self.profile.account_type = "Corporate Savings Account"

    def set_optional_services(self):
        self.profile.optional_services.append("Debit Card")
        self.profile.optional_services.append("Mobile Banking")
        self.profile.optional_services.append("Internet Banking")

    def build(self):
        return self.profile

class CustomerDirector:
    def __init__(self, builder: CustomerBuilder):
        self.builder = builder

    def construct_customer(self, name, credit_score):
        self.builder.set_name(name)
        self.builder.verify_kyc()
        self.builder.set_credit_score(credit_score)
        self.builder.set_account_type()
        self.builder.set_optional_services()
        return self.builder.build()

retail_builder = RetailCustomerBuilder()
director = CustomerDirector(retail_builder)
cust_data = director.construct_customer("Akhil", 700)
print(cust_data)
