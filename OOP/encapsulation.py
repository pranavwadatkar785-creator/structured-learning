class Atm:

    __counter = 100
    # constructor
    def __init__(self):
        self.__pin = ""  # double underscore to make the attributes private now it's memory location name is -> _Atm__balance
        self.__balance = 0 
        self.cid = Atm.__counter
        Atm.__counter +=1
        self.menu()

    #utility functions
    @staticmethod
    def get_counter():
        return Atm.__counter

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if type(new_balance) == int:
            self.__balance = new_balance
        else:
            print("Enter correct value")

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
        self.__pin = user_input
        user_balance = int(input("Enter your balance: "))
        self.__balance = user_balance
        print("pin created successfully.")
        self.menu()

    def change_pin(self):
        user_input = input("Enter your old pin: ")
        if self.__pin == user_input:
            new_pin = input("Enter your new pin: ")
            self.__pin = new_pin
            print("Print changed successfully.")
        else:
            print("Pin Wrong.")
        self.menu()
            
    def check_balance(self):
        user_pin = input("Enter Pin: ")
        if self.__pin == user_pin:
            print(self.__balance,"Rs")
        else:
            print("Wrong Pin.")
        self.menu()

    def withdraw(self):
        user_pin = input("Enter Pin: ")
        if self.__pin == user_pin:
            amount = int(input("Enter amount to withdraw: "))
            if self.__balance<amount:
                print("Not enough balance.")
            else:
                self.__balance = self.__balance - amount
                print(f"{amount} Amount withdrawn.")
        else:
            print("Wrong Pin.")
        self.menu()


p1 = Atm()
p2 = Atm()
p3 = Atm()
