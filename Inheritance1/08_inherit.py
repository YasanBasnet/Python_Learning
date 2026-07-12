class Employee:
    def show_details(self):
        print("This is Parent Method")
    pass
class Developer(Employee):
    pass
d1 = Developer()
d1.show_details()
#same name different arguments is called method overloading it is not in python
#method overriding
class Employee:
    def show_details(self):
        print("This is parent Method")
class Developer:
    def show_details(self):
        print("This is the child Class")
d1 = Developer()
d1.show_details()

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


