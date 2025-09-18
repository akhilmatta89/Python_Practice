"""
Create a base class Employee with:

Method work() → prints "Employee is working"

Method show_salary() → prints "Salary is confidential"

Create a derived class Manager that:

Inherits from Employee

Has its own method manage() → prints "Manager is managing the team"

Overrides the method show_salary() to print "Manager's salary is 1,00,000"

"""


class Employee:

    def work(self):
        print("Employee is working")

    def show_salary(self):
        print("Salary is confidential")


class Manager(Employee):
    def manage(self):
        print("Manager is managing the team")

    def show_salary(self):
        print("Manager's salary is 1,00,000")


class Supervisor(Employee):
    def supervising(self):
        print("Supervisor is supervising the team")


e = Employee()
e.work()
e.show_salary()

m = Manager()
m.manage()
m.show_salary()

s = Supervisor()
s.supervising()
s.show_salary()

