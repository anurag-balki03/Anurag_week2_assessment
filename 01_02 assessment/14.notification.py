class Notification:
    def send(self):
        print("Notification Alert")

class SMSNotification(Notification):
    def __init__(self,message):
        self.message=message
    
    def send(self):
        super().send()
        print(f"the message sent in SMS is: {self.message}")

class EmailNotification(Notification):
    def __init__(self,message):
        self.message=message
    
    def send(self):
        print(f"the message sent in Email is: {self.message}")

S=SMSNotification("this is an SMS")
E=EmailNotification("this is an EMAIL")
S.send()
E.send()
