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
    def __init__(self):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        Student.__init__(self, num1, num2)

    def display(self):
        print("First Number:", self.num1)
        print("Second Number:", self.num2)

obj = Child()
obj.display()