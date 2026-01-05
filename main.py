from FoodItem import FoodItem
from Order import Order
from OrderService import OrderService
from CouponService import CouponService

menu = [
    # 🍕 Pizzas
    FoodItem("Margherita Pizza", 220),
    FoodItem("Farmhouse Pizza", 280),
    FoodItem("Pepperoni Pizza", 320),

    # 🍔 Burgers
    FoodItem("Classic Veg Burger", 140),
    FoodItem("Cheese Burger", 170),
    FoodItem("Chicken Burger", 190),

    # 🍝 Pasta
    FoodItem("White Sauce Pasta", 210),
    FoodItem("Red Sauce Pasta", 200),
    FoodItem("Chicken Alfredo Pasta", 260),

    # 🌮 Starters
    FoodItem("French Fries", 120),
    FoodItem("Garlic Bread", 150),
    FoodItem("Chicken Wings", 280),

    # 🥤 Beverages
    FoodItem("Coca Cola", 60),
    FoodItem("Cold Coffee", 110),
    FoodItem("Fresh Lime Soda", 80),

    # 🍰 Desserts
    FoodItem("Chocolate Brownie", 140),
    FoodItem("Ice Cream Sundae", 160)
]

print("Welcome to Online Food Ordering System 🍔")

cart = {}

print("\n--- MENU ---")
for i, item in enumerate(menu, start=1):
    print(f"{i}. {item.get_name()} - ₹{item.get_price()}")

while True:
    choice = input("\nEnter item number (or 'done'): ")

    if choice.lower() == "done":
        break

    if not choice.isdigit():
        print("Invalid input")
        continue

    index = int(choice) - 1
    if index < 0 or index >= len(menu):
        print("Invalid item number")
        continue

    qty = int(input("Enter quantity: "))
    item = menu[index]

    cart[item] = cart.get(item, 0) + qty
    print(f"{item.get_name()} x {qty} added")

if not cart:
    print("No items selected. Exiting.")
    exit()

order = Order(cart)
order.show_cart_summary()

coupon = input("\nEnter coupon code (or press Enter to skip): ").upper()
if coupon:
    discount = CouponService.apply_coupon(coupon, order._total_amount)
    order.apply_discount(discount)
    print(f"Discount Applied: ₹{discount}")

print(f"Final Amount: ₹{order.get_final_amount()}")

print("\nChoose payment method:")
print("1. UPI")
print("2. CARD")
payment_choice = input("Enter choice: ")

payment_type = "UPI" if payment_choice == "1" else "CARD"

service = OrderService()
service.process_order(order, payment_type)

print("\nFinal Order Status:", order.get_status().value)
print("Thank you for ordering 🙌")
