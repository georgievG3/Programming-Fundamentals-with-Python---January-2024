bakery_stock = {}
sold_food = 0

while True:
    command = input()

    if command == "Complete":
        break

    action, quantity, food = command.split()

    if action == "Receive":

        if int(quantity) > 0:

            if food not in bakery_stock:
                bakery_stock[food] = 0

            bakery_stock[food] += int(quantity)

    elif action == "Sell":

        if food not in bakery_stock:
            print(f"You do not have any {food}.")
            continue

        if int(quantity) > bakery_stock[food]:
            sold_quantity = bakery_stock[food]
            sold_food += sold_quantity

            del bakery_stock[food]

            print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")

        else:
            bakery_stock[food] -= int(quantity)
            sold_food += int(quantity)

            print(f"You sold {quantity} {food}.")

            if bakery_stock[food] == 0:
                del bakery_stock[food]

for food_stock, quantity_stock in bakery_stock.items():
    print(f"{food_stock}: {quantity_stock}")

print(f"All sold: {sold_food} goods")