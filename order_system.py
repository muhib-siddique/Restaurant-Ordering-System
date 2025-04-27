menu = {
    'Pizza': 50,
    'Pasta': 60,
    'Lasagnia': 70,
    'Burger': 80,
    'Cold coffee': 40
}

print("Welcome To Mosi Restaurant 🍽️")
print("\nMenu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# First Item
item_1 = input("\nEnter the name of the item you want to order: ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"✅ {item_1} has been added to your order.")
else:
    print(f"❌ Sorry, {item_1} is not available.")

# Another Item
another_order = input("\nDo you want to add another item? (Yes/No): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of your next item: ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"✅ {item_2} has been added to your order.")
    else:
        print(f"❌ Sorry, {item_2} is not available.")

print(f"\n🧾 Your total bill is: Rs {order_total}")
print("Thank you for ordering from Mosi Restaurant! 🙏")
