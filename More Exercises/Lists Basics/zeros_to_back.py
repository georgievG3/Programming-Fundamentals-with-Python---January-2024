# integer_list = list(map(int, input().split(", ")))
# for number in integer_list:
#     if number == 0:
#         integer_list.remove(number)
#         integer_list.append(0)
#
# print(integer_list)

integers_as_list = [int(num) for num in input().split(", ")]

zeros = integers_as_list.count(0)
zeros_list = [0] * zeros
integers_with_no_zeros = [num for num in integers_as_list if not num == 0]
final_list = integers_with_no_zeros + zeros_list
print(final_list)

