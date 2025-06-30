from abc import abstractmethod, ABC


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPall(PaymentProcessor):
    def pay(self):
        print("PayPal payment processed")
class CreditCard(PaymentProcessor):
    def pay(self):
        print("Credit card payment processed")

class Crypto(PaymentProcessor):
    def pay(self):
        print("Crypto payment processed")

if __name__ == '__main__':
    paypall = PayPall()
    credit_card = CreditCard()
    crypto = Crypto()

    payment_processors = [paypall, credit_card, crypto]

    for payment_processor in payment_processors:
        payment_processor.pay()