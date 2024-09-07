string = input()

while True:
    command = input()

    if command == "Travel":
        break

    actual_command = command.split(":")
    action = actual_command[0]

    if action == "Add Stop":
        index = int(actual_command[1])
        substring = actual_command[2]

        if index in range(len(string)):
            string = string[:index] + substring + string[index:]

    elif action == "Remove Stop":
        start_index = int(actual_command[1])
        end_index = int(actual_command[2])

        if start_index in range(len(string)) and end_index in range(len(string)):
            string = string[:start_index] + string[end_index + 1:]

    elif action == "Switch":
        old_string = actual_command[1]
        new_string = actual_command[2]

        if old_string in string:
            string = string.replace(old_string, new_string)

    print(string)

print(f"Ready for world tour! Planned stops: {string}")
