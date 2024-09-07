def factorial(number_one, number_two):
    first_result = 1
    second_result = 1

    for number in range(1, number_one + 1):
        first_result = first_result * number

    for number in range(1, number_two + 1):
        second_result = second_result * number

    return f"{first_result / second_result:.2f}"

first_integer = int(input())
second_integer = int(input())
print(factorial(first_integer, second_integer))