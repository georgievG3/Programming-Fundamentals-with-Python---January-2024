list_of_gifts = input().split()

command = input()
while command != "No Money":
    command_as_list = command.split()
    if command_as_list[0] == "OutOfStock":
        if command_as_list[1] in list_of_gifts:
            list_of_gifts = [gift.replace(command_as_list[1], 'None') for gift in list_of_gifts]
        else:
            pass
    elif command_as_list[0] == "Required":
        if int(command_as_list[2]) in range(len(list_of_gifts)):
            list_of_gifts.pop(int(command_as_list[2]))
            list_of_gifts.insert(int(command_as_list[2]), command_as_list[1])
        else:
            pass
    elif command_as_list[0] == "JustInCase":
        list_of_gifts.pop()
        list_of_gifts.append(command_as_list[1])
    command = input()
for _ in list_of_gifts:
    if "None" in list_of_gifts:
        list_of_gifts.remove("None")
print(" ".join(list_of_gifts))
# list_of_gifts = input().split()
#
# command = input()
# while not command == "No Money":
#     command = command.split()
#     real_command = command[0]
#     if real_command == "OutOfStock":
#         gift = command[1]
#         for index in range(len(list_of_gifts)):
#             if list_of_gifts[index] == gift:
#                 list_of_gifts[index] = "None"
#     elif real_command == "Required":
#         gift = command[1]
#         index = int(command[2])
#         if index in range(len(list_of_gifts)):
#             list_of_gifts[index] = gift
#     elif real_command == "JustInCase":
#         gift = command[1]
#         list_of_gifts.pop(-1)
#         list_of_gifts.append(gift)
#     command = input()
#
# final_list = [gift for gift in list_of_gifts if not gift == "None"]
#
# print(*final_list, sep=" ")