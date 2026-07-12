# Multiple Inheritance
class Employee:
    def __init__(self):
        self.user = "Ram"
        self.address = "Kathmandu"
class EmailSend:
    def send_email(self):
        pass
class Developer(Employee , EmailSend):
    pass
d1 = Developer()
print(d1.user)

# Multi level
class Employee:
    def __init__(self):
        self.user = "Ram"
        self.address = "Kathmandu"
class EmailSend(Employee):
    def send_email(self):
        pass
class Developer(EmailSend):
    pass
d1 = Developer()
print(d1.user)

# Hierarchical Inheritance
class Employee:
    def __init__(self):
        self.user = "Ram"
        self.address = "Kathmandu"

class EmailSend(Employee):
    pass

class Developer(Employee):
    pass

e1 = EmailSend()
d1 = Developer()

print(e1.user)
print(d1.user)

# Single
class Student:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

class Child(Student):
    def display(self):
        print("First Number:", self.num1)
        print("Second Number:", self.num2)



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

obj = Child(num1, num2)
obj.display()

# Hybrid Inheritance
# Base class
class A:
    def displayA(self):
        print("This is Class A")

# Hierarchical inheritance
class B(A):
    def displayB(self):
        print("This is Class B")

class C(A):
    def displayC(self):
        print("This is Class C")

# Multiple inheritance
class D(B, C):
    def displayD(self):
        print("This is Class D")

# Object of D
obj = D()

obj.displayA()
obj.displayB()
obj.displayC()
obj.displayD()


