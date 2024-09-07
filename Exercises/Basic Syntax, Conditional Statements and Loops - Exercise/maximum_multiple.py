divisor = int(input())
boundary = int(input())

number = 0
for numbers in range(boundary, 0, -1):
    if numbers % divisor == 0:
        number = numbers
        break
print(number)
