"""
- This is a creational design pattern which provides an interface for creating objects in superclass
    but allows subclasses to alter the type of objects that will be created.

- Provides a way to create objects without exposing the creation logic to the client.

- Instead of calling a class constructor directly, you delegate object creation to a factory.

- This is especially useful when:
    - You have multiple subclasses implementing the same interface.
    - You want to centralize and control object creation.
    - You want to avoid cluttering your code with if/elif blocks everywhere.
"""

"""
Imagine you're building an e‑commerce platform.
Users can pay using:
    - Credit Card
    - PayPal
    - Bank Transfer
"""

# Without FactoryMethod
#-------------------------

class CreditCardPaymentService:
    pass
class PaypalPaymentService:
    pass
class BankTransferService:
    pass

# client calls like this
service_type = input("Enter the type of service you want: ")
if service_type == "credit":
    service = CreditCardPaymentService()
elif service_type == "paypal":
    service = PaypalPaymentService()
elif service_type == "bank":
    service = BankTransferService()


# With FactoryMethod
#-------------------------

# STEP-1: we will create a common interface
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# STEP-2: we create concrete implementations
class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"initiated credit card payment for {amount} euros")

class PaypalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"initiated paypal payment for {amount} euros")

class BankTransferPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"initiated bank transfer payment for {amount} euros")

# STEP-3: her we build the factory
class PaymentFactory:

    @staticmethod
    def get_payment_processor(method_type):
        if method_type.lower() == "credit":
            return CreditCardPayment()
        elif method_type.lower() == "paypal":
            return PaypalPayment()
        elif method_type.lower() == "bank":
            return BankTransferPayment()
        else:
            raise ValueError("Invalid payment method type")

#STEP-4: Client code uses the factory
payment_factory = PaymentFactory()
payment_processor = payment_factory.get_payment_processor("bank")
payment_processor.pay(100)