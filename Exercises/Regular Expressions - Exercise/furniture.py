import re

total_cost = 0
bought_furniture = []

text = input()
while text != "Purchase":
    pattern = r"\>>([A-Za-z]+)<<(\d+\.?\d+)\!(\d+)"
    match = re.search(pattern, text)

    if match:
        furniture, price, quantity = match.groups()

        bought_furniture.append(furniture)
        total_cost += int(quantity) * float(price)

    text = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")