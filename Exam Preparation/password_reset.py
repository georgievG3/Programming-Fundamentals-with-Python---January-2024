raw_password = input()

while True:
    command = input()

    if command == "Done":
        break

    action = command.split()

    if action[0] == "TakeOdd":
        new_password = ""

        for i in range(1, len(raw_password), 2):
            new_password += raw_password[i]

        raw_password = new_password

        print(raw_password)

    elif action[0] == "Cut":
        index = int(action[1])
        length = int(action[2])

        substring = raw_password[index:(index + length)]

        raw_password = raw_password.replace(substring, "", 1)

        print(raw_password)

    elif action[0] == "Substitute":
        substring = action[1]
        substitute = action[2]

        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)

        else:
            print("Nothing to replace!")

print(f"Your password is: {raw_password}")
