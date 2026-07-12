# class Student:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#     def show_details(self , age):
#         print(f"My name is  {self.name} and age is {age}")
# s1 = Student("Yasan","Pyuthan")
# s1.show_details(21
# class EmailValidation:
#     def __init__(self, email):
#         self.email = email

#     def check(self):
#         if "@"  in self.email: 
#             print("valid Email")
#         elif  any(ch.isupper() for ch in self.email):
#             print("valid Email")
#         else:
#             print("InValid Email.")

# email = input("Enter your email: ")
# obj = EmailValidation(email)
# obj.check()

# def func1(*args , **kwargs):
#     print(args)
#     print(kwargs)
# func1(10 , 11 , name1 = "yasan" , address = "Pyuthan")

class Class1:
    def sum(self, *args):
        total = 0
        for i in args:
            total += i
        print("Sum:", total)

    def display(self, **kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)


obj = Class1()

obj.sum(10, 20, 30, 40)

obj.display(
    name="Yasan",
    address="Pokhara",
    age=20,
    college="Pokhara University"
)
obj.display(
    name="Yasan",
    address="Pokhara",
    age=20,
    college="Pokhara University"
)