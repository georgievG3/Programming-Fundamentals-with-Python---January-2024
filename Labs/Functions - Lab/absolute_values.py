numbers = input()
absolute_numbers = list(abs(float(number)) for number in numbers.split(" "))
print(absolute_numbers)


# numbers = input().split()
#
# absolute_numbers = []
# for number in numbers:
#     absolute_numbers.append(abs(float(number)))
#
# print(absolute_numbers)
