string = input().split()

even_list = [word for word in string if len(word) % 2 == 0]
for word in even_list:
    print(word)

# print("\n".join(even_list))