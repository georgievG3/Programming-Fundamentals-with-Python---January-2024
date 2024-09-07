numbers = input().split()
even_numbers_list = []

def check_even_numbers(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False

even_numbers = filter(check_even_numbers, numbers)

for number in even_numbers:
    even_numbers_list.append(int(number))

print(even_numbers_list)

# nums = [int(el) for el in input().split()]
# even_numbers = filter(lambda num: num % 2 == 0, nums)
# print(list(even_numbers))