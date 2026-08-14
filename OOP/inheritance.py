#Single Inheritance
class User:

    def __init__(self):
        self.name = "Pranav"

    def login(self):
        print("login")

    def register(self):
        print("register")

class Student(User):

    def __init__(self):
        super().__init__()
        self.rollno = 101

    def enroll(self):
        print("Enroll into course")

#Multilevel Inheritance
class Otherclass(Student):
    pass


u = User()
s = Student()
o = Otherclass()
print(u.name)
print(s.name)
print(o.name)

# Heirarchial Inheritance one parent more than one child
class Onemore(User):
    pass

# Multiple Inheritance One child multiple parent
class Child(User,Student):
    # If there are same methods in both the class User & Student method of User will be called by Child class Because user is return 1st
    pass

# Hybrid Inheritance More than one type inheritance combined