class Shpae:

    # method overloading same method name but different parameters differentiate methods
    # but it will not work in python 
    # def area(self, radius):
    #     return 3.14*(radius**2)

    # def area(self, l, b):
    #     return l*b
    # this type of logic to perform method overloading
    def area(self, a, b=0):
        if b==0:
            return 3.14*a*a
        else:
            return a*b

class Fisrt:

    def m1(self):
        return "M1"

class Second(Fisrt):

    def m1(self):
        return "M1 from Second"

s = Second()
# object of Second class overrides the method of Fisrt class 
print(s.m1())