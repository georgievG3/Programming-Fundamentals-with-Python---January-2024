my_list = []

for part in range(3):
    part_of_body = input()
    my_list.append(part_of_body)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)
      