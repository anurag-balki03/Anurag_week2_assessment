from abc import ABC,abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def __init__(self,name):
        self.username=name
        
    def login(self):
        print(f"{self.username} has logged into GOOGLE sucessfully")
        
    def logout(self):
        print(f"{self.username} is logged out from GOOGLE")

class FacebookAuth(UserAuthentication):
    def __init__(self,name):
        self.username=name
        
    def login(self):
        print(f"{self.username} has logged into FACEBOOK sucessfully")
        
    def logout(self):
        print(f"{self.username} is logged out from FACEBOOK")

Google=GoogleAuth("YAMEN")
Facebook=FacebookAuth("RAMEN")
Google.login()
Facebook.login()
Google.logout()
Facebook.logout()
