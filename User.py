class User:
    def __init__(self,name):
        self._name = name
    
    def place_order(self, order):
        order.confirm_order()

