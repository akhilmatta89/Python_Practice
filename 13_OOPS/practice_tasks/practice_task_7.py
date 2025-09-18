"""
Practice Task 8: Multilevel Inheritance
Create the following chain:

Base class: Device → method: power_on() → "Device powered on"

Derived class: Computer → method: boot() → "Computer is booting"

Further derived class: Laptop → method: fold() → "Laptop is folded"

Then create an object of Laptop and call all three methods.

"""
class Device:
    def power_on(self):
        print("Device powered on")

class Computer(Device):
    def boot(self):
        print("Computer is booting")

class Laptop(Computer):
    def fold(self):
        print("Laptop is folded")

l = Laptop()
l.fold()
l.power_on()
l.boot()