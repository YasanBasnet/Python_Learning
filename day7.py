# class College:
#     College_name = "Everest Engineering College"

#     def __init__(self, location):
#         self.location = location

#     def show_details(self):
#         print("College Name:", College.College_name)
#         print("Location:", self.location)

# c1 = College("Sanepa Height")
# c2 = College("Kalanki")

# print(College.College_name)
# print(c1.College_name)
# print(c1.location)
# print(c2.location)

# setattr, getattr, hasattr
#setattr(object, attribute_name, new_value)
#getattr(object, attribute_name, default_vaule if need)
#hasattr(object, attribute_name)give True or false if attribute exist give true else false
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Yasan")

# print("Name:", getattr(s1, "name"))
# print("Does age exist?", hasattr(s1, "age"))
# print("Age:", getattr(s1, "age", "Age not found"))

# setattr(s1, "age", 20)

# print("Does age exist now?", hasattr(s1, "age"))
# print("Age:", getattr(s1, "age"))

class Employee:
    def __init__(self, details):
        # Set attributes from dictionary
        for key, value in details.items():
            setattr(self, key, value)

    def update(self):
        key = input("Enter key to update (name/department/salary): ")

        if hasattr(self, key):
            value = input("Enter new value: ")

            if key == "salary":
                value = int(value)

            setattr(self, key, value)
            print("Updated Successfully!")
        else:
            print("Invalid Key")

    def display(self):
        print("Name:", getattr(self, "name"))
        print("Department:", getattr(self, "department"))
        print("Salary:", getattr(self, "salary"))

details = {
    "name": "Dikshya",
    "department": "IT",
    "salary": 50000
}

emp = Employee(details)

print("Before Update")
emp.display()
emp.update()
print("After Update")
emp.display()