def perfect_number_validator(number):
    sum_numbers = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            sum_numbers += divisor

    if sum_numbers == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(perfect_number_validator(num))