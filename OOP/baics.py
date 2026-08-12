class Atm:
    # constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
            How can i Help You?
            1. Create Pin
            2. Change Pin
            3. Check Balance
            4. Withdraw
            5. Anything to Exit
            ===========================================
        """)

        if user_input == "1":
            #create pin
            self.create_pin()
        elif user_input == "2":
            #change pin
            self.change_pin()
        elif user_input == "3":
            #check balance
            self.check_balance()
        elif user_input == "4":
            #withdraw
            self.withdraw()
        else:
            return "End"

    def create_pin(self):
        user_input = input("Enter your pin: ")
        self.pin = user_input
        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance
        print("pin created successfully.")
        self.menu()

    def change_pin(self):
        user_input = input("Enter your old pin: ")
        if self.pin == user_input:
            new_pin = input("Enter your new pin: ")
            self.pin = new_pin
            print("Print changed successfully.")
        else:
            print("Pin Wrong.")
        self.menu()
            

    def check_balance(self):
        user_pin = input("Enter Pin: ")
        if self.pin == user_pin:
            print(self.balance,"Rs")
        else:
            print("Wrong Pin.")
        self.menu()

    def withdraw(self):
        user_pin = input("Enter Pin: ")
        if self.pin == user_pin:
            amount = int(input("Enter amount to withdraw: "))
            if self.balance<amount:
                print("Not enough balance.")
            else:
                self.balance = self.balance - amount
                print(f"{amount} Amount withdrawn.")
        else:
            print("Wrong Pin.")
        self.menu()

# obj = Atm()
# print(obj.pin,obj.balance)

class Fraction:

    #parameterized constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den

        return f"{new_num}/{new_den}"

    def __sub__(self, other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        
        return f"{new_num}/{new_den}"

    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        
        return f"{new_num}/{new_den}"

    def __truediv__(self, other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        
        return f"{new_num}/{new_den}"

    def convert_to_decimal(self):
        return self.num/self.den

fr1 = Fraction(1,4)
fr2 = Fraction(1,4)
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1.convert_to_decimal())