class Order:
    def __init__(self,items):
        self._items = items
        self._total_amt = 0
        self._calculate_total()

    def _calculate_total(self):
        for item in self._items:
            self._total_amount += item.get_price()

    def confirm_order(self):
        print(f"Order confirmed. Amount : {self._total_amount}")
    
    def get_total_amount(self):
        return self._total_amount