"""
Singleton ensures a class has only ONE instance in the entire application, and provides a global access point to it.

In a banking system, some components must exist only once, such as:
    - A central logging system
    - A database connection manager
    - A configuration manager
    - A transaction audit tracker
    - A risk engine context

You don’t want multiple instances of these floating around — it would cause chaos.

Singleton ensures there is exactly one.

"""

# Lets see single configuration in the banking system
class CentralBankConfig:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set_key(self, key, value):
        self.settings[key] = value

    def get_key(self, key):
        return self.settings[key]


c_bank = CentralBankConfig()
c_bank.set_key("name", "akhil")
print(c_bank.settings)

c_bank_2 = CentralBankConfig()
if c_bank is c_bank_2:
    print("both are same")