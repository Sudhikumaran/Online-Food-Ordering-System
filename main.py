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
    FoodItem("Pizza", 250),
    FoodItem("Burger", 150),
    FoodItem("Pasta", 200)
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
