from abc import ABC ,abstractmethod

class FuturePlan(ABC): # dont create object for abstract class
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass

    def order(self):
        pass

# for developer child class     you cant run this code without implement abstract method

class webapp(FuturePlan):
    def profile(self):
        print("your profile is cerated :")
    
    def login(self):
        print("webApp is login ")

    def logout(self):
        print("webApp is logout")

obj=webapp()
obj.profile()
obj.login()
obj.logout()

