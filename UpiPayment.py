from Payment import Payment
class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")
