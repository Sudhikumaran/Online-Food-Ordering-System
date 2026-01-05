import Payment
class UpiPayment(Payment):
    def Pay(self, amount):
        print(f"Paid {amount} using UPI")
