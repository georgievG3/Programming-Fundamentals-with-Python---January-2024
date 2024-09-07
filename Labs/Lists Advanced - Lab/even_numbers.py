list_of_number = [int(x) for x in input().split(", ")]

even_number_indices = [index for index in range(len(list_of_number)) if list_of_number[index] % 2 == 0]
print(even_number_indices)