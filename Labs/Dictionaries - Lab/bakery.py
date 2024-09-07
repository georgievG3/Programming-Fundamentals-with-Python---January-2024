stock_bakery = input().split(" ")
stock_dict = {}

for i in range(0, len(stock_bakery), 2):
    key = stock_bakery[i]
    value = stock_bakery[i + 1]
    stock_dict[key] = int(value)

print(stock_dict)
