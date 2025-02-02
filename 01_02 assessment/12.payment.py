class payment_process:
    def payment(self):
        print("payment process is sucessfully initiated")
        
class CreditCardPayment(payment_process):
    def payment(self):
        super().payment()
        print("Your payment is sucessfull. Payment is done through CREDIT CARD")
        
class PayPayPayment(payment_process):
    def payment(self):
        super().payment()
        print("Your payment is sucessfull. Payment is done through PAYPAL")
        
class BitCoinPayment(payment_process):
    def payment(self):
        super().payment()
        print("Your payment is sucessfull. Payment is done through BITCOIN")
        
cred=CreditCardPayment()
paypal=PayPayPayment()
Bitcoin=BitCoinPayment()
cred.payment()
paypal.payment()
Bitcoin.payment()
        