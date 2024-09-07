# list_as_integer = ([int(number) for number in input().split(" ")])
# count_of_numbers = int(input())
#
# for numbers in range(count_of_numbers):
#     sorted_list = sorted(list_as_integer)
#     sorted_list.reverse()
#     lowest_number = sorted_list.pop()
#     list_as_integer.remove(lowest_number)
# list_as_string = map(str, list_as_integer)
# print(", ".join(list_as_string))
list_as_integer = ([int(number) for number in input().split(" ")])
count_of_numbers = int(input())

for numbers in range(count_of_numbers):
    list_as_integer.remove(min(list_as_integer))

print(*list_as_integer, sep=', ')
