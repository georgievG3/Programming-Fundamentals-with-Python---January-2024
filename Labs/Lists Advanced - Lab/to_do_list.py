to_do_list = [0] * 10
command = input()

while command != "End":
    tokens = command.split("-")
    importance = int(tokens[0]) - 1
    note = tokens[1]
    to_do_list.pop(importance)
    to_do_list.insert(importance, note)

    command = input()

result = [element for element in to_do_list if element != 0]
print(result)

