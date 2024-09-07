# def calculation(operator, num1, num2):
#     if operator == "multiply":
#         return multiply_numbers(operator, num1, num2)
#     elif operator == "divide":
#         return divide_numbers(operator, num1, num2)
#     elif operator == "add":
#         return add_numbers(operator, num1, num2)
#     elif operator == "subtract":
#         return subtract_numbers(operator, num1, num2)
#
# def multiply_numbers(operator, num1, num2):
#     result = num1 * num2
#     return result
#
# def divide_numbers(operator, num1, num2):
#     result = num1 // num2
#     return result
#
# def add_numbers(operator, num1, num2):
#     result = num1 + num2
#     return result
#
# def subtract_numbers(operator, num1, num2):
#     result = num1 - num2
#     return result
#
# input_operator = input()
# number_one = int(input())
# number_two = int(input())
#
# print(calculation(input_operator, number_one, number_two))

def calculation(operator, num1, num2):
    result = None
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 // num2
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2

    return result

input_operator = input()
number_one = int(input())
number_two = int(input())
print(calculation(input_operator, number_one, number_two))