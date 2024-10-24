# Define thee menu of the resturant
menu = {
    "Pizza" : 2000,
    "Pasta" : 1500,
    "Burger" : 700,
    "Loaded Fries" : 800,
    "Salad" : 300,
    "Coffee" : 400,
    "Tea" : 100
}

# Greet
print("Welcome To The PYTHON Resturant")
print("Pizza: 2000\nPasta: 1500\nBurger: 700\nLoaded Fries: 800\nSalad: 300\nCoffee: 400\nTea: 100")

order_total = 0
# like 700 + 800 = 1500
item_1 = input("Enter the name of the item you want to order...")
if item_1 in menu:
    order_total += menu[item_1] #0+2000
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Order item {item_1} not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter your second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your second item {item_2} has been added to your order")
    else:
        print(f"Second item {item_2} is not available yet!")

print(f"Total amount of items to pay {order_total}")
