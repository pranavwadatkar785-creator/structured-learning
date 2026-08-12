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

obj = Atm()
print(obj.pin,obj.balance)