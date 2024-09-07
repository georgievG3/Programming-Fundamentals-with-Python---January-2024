string = input()

my_list = string.split(" ")
inverted_list = []

for i in my_list:
    strings_as_number = int(i) * -1
    inverted_list.append(strings_as_number)
print(inverted_list)
