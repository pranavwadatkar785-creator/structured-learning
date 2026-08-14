class Customer:

    def __init__(self,name,gender,address):
        self.__name = name
        self.__gender = gender
        self.__address = address

    def print_profile(self):
        print(self.__name)
        print(self.__gender)
        print(self.__address.get_city(), self.__address.pincode, self.__address.state)

    def edit_profile(Self, new_name, new_city, new_pin, new_state):
        Self.__name = new_name
        Self.__address.edit_address(new_city, new_pin, new_state)


class Address:

    def __init__(self,city,pincode,state):
        self.__city = city
        self.__pincode = pincode
        self.__state = state

    def get_city(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.__pincode = new_pin
        self.__state = new_state

add1 = Address("Pune", 411062, "Maharashtra")
cus1 = Customer("Pranav", "Male", add1)
#cus1.print_address() #error because city is private attribute to access it create a getter method
cus1.edit_profile("Pranav Wadatkar", "Moshi", 411062, "Maharashtra")
cus1.print_profile()