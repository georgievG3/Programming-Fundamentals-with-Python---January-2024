def sum_numbers(num1, num2):

    return num1 + num2

def subtract(num1, num2, num3):
    result = (num1 + num2) - num3
    return result

def add_and_subtract(num1, num2, num3):
    sum_numbers(num1, num2)
    subtract(num1, num2, num3)

    return subtract(num1, num2, num3)

first_integer = int(input())
second_integer = int(input())
third_integer = int(input())
print(add_and_subtract(first_integer, second_integer, third_integer))