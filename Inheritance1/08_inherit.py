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


