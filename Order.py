from OrderStatus import OrderStatus

class Order:
    def __init__(self, cart):
        self._cart = cart          # {FoodItem: quantity}
        self._total_amount = 0
        self._discount = 0
        self._status = OrderStatus.CREATED
        self._calculate_total()

    def _calculate_total(self):
        self._total_amount = 0
        for item, qty in self._cart.items():
            self._total_amount += item.get_price() * qty

    def show_cart_summary(self):
        print("\n--- CART SUMMARY ---")
        for item, qty in self._cart.items():
            print(f"{item.get_name()} x {qty} = ₹{item.get_price() * qty}")
        print(f"Subtotal: ₹{self._total_amount}")

    def apply_discount(self, discount):
        self._discount = discount

    def get_final_amount(self):
        return self._total_amount - self._discount

    def confirm_order(self):
        self._status = OrderStatus.CONFIRMED
        print(f"Order confirmed. Amount: ₹{self._total_amount}")

    def mark_paid(self):
        self._status = OrderStatus.PAID
        print("Order payment successful")

    def get_status(self):
        return self._status
