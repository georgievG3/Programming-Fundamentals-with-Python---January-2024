bakery = {}

while True:
    command = input()

    if command == "statistics":
        break

    key, value = command.split(": ")

    if key not in bakery:
        bakery[key] = 0
    bakery[key] += int(value)

print("Products in stock:")
for product, quantity in bakery.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(bakery.keys())}\nTotal Quantity: {sum(bakery.values())}")