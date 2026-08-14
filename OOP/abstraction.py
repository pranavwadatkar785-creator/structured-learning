from abc import ABC,abstractmethod

class BankApp(ABC): 

    def database(Self):
        print("Connect to db")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):

    def mobile_login(Self):
        print("Login to mobile")

    # no object can be created using MobileApp because MobileApp does not have any method security 
    def security(self):
        print
