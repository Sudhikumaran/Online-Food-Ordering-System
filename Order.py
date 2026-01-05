from OrderStatus import OrderStatus

class Order:
    def __init__(self, items):
        self._items = items
        self._total_amount = 0
        self._status = OrderStatus.CREATED
        self._calculate_total()

    def _calculate_total(self):
        for item in self._items:
            self._total_amount += item.get_price()

    def confirm_order(self):
        self._status = OrderStatus.CONFIRMED
        print(f"Order confirmed. Amount: {self._total_amount}")

    def mark_paid(self):
        self._status = OrderStatus.PAID
        print("Order payment successful")

    def get_total_amount(self):
        return self._total_amount

    def get_status(self):
        return self._status
