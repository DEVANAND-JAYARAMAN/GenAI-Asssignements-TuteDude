from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self,amount):
        print("Credit Card Payment :",amount)

class UPIPayment(Payment):
    def process_payment(self,amount):
        print("UPI Payment :",amount)

obj1=CreditCardPayment()
obj2=UPIPayment()

obj1.process_payment(1500)
obj2.process_payment(800)