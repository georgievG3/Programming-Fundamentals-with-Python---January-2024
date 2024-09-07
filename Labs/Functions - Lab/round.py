numbers = input()

result = list(round(float(number)) for number in numbers.split(" "))
print(result)