# class Student:
#     def user_data(self):
#         print("this is user details.")
# s1 = Student()
# s1.user_data()

# class Building:
#     def building_height(self):
#         name = input("Enter the building height")
#         print(f"the building height is {name}")
# Building().building_height()
# class Student:
#     def __init__(self, name):
#         self.name = name
#     def user_detail(self):
#      print(f"this is user details of {self.name}")

# s1 = Student("ram")
# s1.user_detail()


# class Student:
#     def __init__(self, name):
#         self.name = name

#     def user_detail(self):
#         print(f"Student name is  {self.name}")

# name = input("Enter student name: ")

# s1 = Student(name)
# s1.user_detail()

class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return  self.name
s1 = Student("Ram")
print(s1)