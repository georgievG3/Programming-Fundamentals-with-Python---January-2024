def calculate_total_price(product, quantity):
    total_price = None
    if product == "coffee":
        total_price = quantity * 1.50
    elif product == "coke":
        total_price = quantity * 1.40
    elif product == "water":
        total_price = quantity * 1.00
    elif product == "snacks":
        total_price = quantity * 2.00

    return total_price

product_type = input()
quantity = int(input())
print(f"{calculate_total_price(product_type, quantity):.2f}")