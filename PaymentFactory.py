from UpiPayment import UpiPayment
from CardPayment import CardPayment

class PaymentFactory:

    @staticmethod
    def get_payment_method(method):
        if method == "UPI":
            return UpiPayment()
        elif method == "CARD":
            return CardPayment()
        else:
            raise ValueError("Invalid payment method")
