from FoodItem import FoodItem
from Order import Order
from User import User
from Payment import Payment
from UpiPayment import UpiPayment
from CardPayment import CardPayment

pizza = FoodItem("Pizza", 250)
burger = FoodItem("Burger", 150)

items = [pizza,burger]
order = Order(items)

user = User("Sudhi")
user.place_order(order)

payment = UpiPayment()
payment.pay(order.get_total_amount())
