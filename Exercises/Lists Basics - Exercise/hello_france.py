items_with_prices_list = input().split("|")
budget = float(input())

MAXIMUM_CLOTHES_PRICE = 50.00
MAXIMUM_SHOES_PRICE = 35.00
MAXIMUM_ACCESSORIES_PRICE = 20.50

bought_items = []
profit = 0
for item_with_price in items_with_prices_list:
    item = item_with_price.split("->")
    product_type = item[0].strip()
    price = float(item[1])
    if product_type == "Clothes" and price <= MAXIMUM_CLOTHES_PRICE and price <= budget:
        bought_items.append(price * 1.40)
        profit += price * 0.40
        budget -= price
    elif product_type == "Shoes" and price <= MAXIMUM_SHOES_PRICE and price <= budget:
        bought_items.append(price * 1.40)
        profit += price * 0.40
        budget -= price
    elif product_type == "Accessories" and price <= MAXIMUM_ACCESSORIES_PRICE and price <= budget:
        bought_items.append(price * 1.40)  # Profit is added only for "Clothes" and "Shoes"
        profit += price * 0.40
        budget -= price

total_winnings = sum(bought_items)
new_budget = total_winnings + budget

if new_budget >= 150:
    print(" ".join([f'{item:.2f}' for item in bought_items]))
    print(f"Profit: {profit:.2f}")
    print("Hello, France!")
else:
    print(" ".join([f'{item:.2f}' for item in bought_items]))
    print(f"Profit: {profit:.2f}")
    print("Not enough money.")
