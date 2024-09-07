def check_number_type(numbers):
    positive_numbers = ", ".join(str(number) for number in numbers if number >= 0)
    print(f"Positive: {positive_numbers}")

    negative_numbers = ", ".join(str(number) for number in numbers if number < 0)
    print(f"Negative: {negative_numbers}")

    even_numbers = ", ".join(str(number) for number in numbers if number % 2 == 0)
    print(f"Even: {even_numbers}")

    odd_numbers = ", ".join(str(number) for number in numbers if number % 2 != 0)
    print(f"Odd: {odd_numbers}")


numbers = list(map(int, input().split(", ")))
check_number_type(numbers)



