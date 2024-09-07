def finds_smallest_number(num1, num2, num3):
    smallest_number = min(num1, num2, num3)

    return smallest_number


first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

print(finds_smallest_number(first_integer, second_integer, third_integer))