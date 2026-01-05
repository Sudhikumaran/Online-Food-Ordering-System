from FoodItem import FoodItem
from Order import Order
from User import User
from OrderService import OrderService

def show_menu(menu):
    print("\n--- MENU ---")
    for idx, item in enumerate(menu, start=1):
        print(f"{idx}. {item._name} - ₹{item.get_price()}")

def take_order(menu):
    selected_items = []
    while True:
        choice = input("Enter item number to add (or 'done' to finish): ")

        if choice.lower() == "done":
            break

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(menu):
                selected_items.append(menu[index])
                print(f"{menu[index]._name} added")
            else:
                print("Invalid item number")
        else:
            print("Invalid input")

    return selected_items


# ----- START -----
print("Welcome to Online Food Ordering System 🍔🍕")

user_name = input("Enter your name: ")
user = User(user_name)

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


show_menu(menu)
items = take_order(menu)

if not items:
    print("No items selected. Order cancelled.")
    exit()

order = Order(items)

print("\nChoose payment method:")
print("1. UPI")
print("2. CARD")

payment_choice = input("Enter choice: ")

payment_type = "UPI" if payment_choice == "1" else "CARD"

service = OrderService()
service.process_order(order, payment_type)

print("\nThank you for ordering! 🙌")
