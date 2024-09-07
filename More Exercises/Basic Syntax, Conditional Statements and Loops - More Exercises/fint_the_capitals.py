sting = input()
indices_list = []

for index in range(len(sting)):
    if sting[index].isupper():
        indices_list.append(index)

print(indices_list)