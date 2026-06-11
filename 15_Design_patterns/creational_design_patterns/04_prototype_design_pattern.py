"""
Prototype Pattern lets you clone existing objects instead of creating new ones from scratch.

It’s useful when:
    Object creation is expensive (heavy initialization, DB calls, API calls)
    You want to create similar objects with small variations
    You want to avoid subclass explosion
    You want to copy objects without exposing complex construction logic

"""
import copy
from abc import ABC, abstractmethod
from distutils.sysconfig import customize_compiler


# STEP-1: Lets create a prototype base class

class PrototypeDesignPatterns(ABC):
    @abstractmethod
    def clone(self):
        pass

class CustomerProfile(PrototypeDesignPatterns):
    def __init__(self,customer_profile, name, account_type, account_number="1234567"):
        self.customer_profile = customer_profile
        self.name = name
        self.account_type = account_type
        self.account_number = account_number

    def clone(self):
        return copy.deepcopy(self)

    def print_info(self):
        print(self.__dict__)


retail_profile = CustomerProfile(customer_profile="Retail", name="akhil", account_type="savings")
retail_profile.print_info()

corporate_template = retail_profile.clone()
corporate_template.customer_profile = "Corporate"
corporate_template.print_info()