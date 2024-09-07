products_dict = {}

while True:
    command = input()

    if command == "buy":
        break

    product, price, quantity = command.split()

    if product not in products_dict:
        products_dict[product] = {"Price": 0, "Quantity": 0}
    products_dict[product]["Price"] = float(price)
    products_dict[product]["Quantity"] += int(quantity)

for prod, quant in products_dict.items():
    print(f"{prod} -> {quant['Price'] * quant['Quantity'] :.2f}")