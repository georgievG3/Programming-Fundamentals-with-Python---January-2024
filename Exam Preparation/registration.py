username = input()

while True:
    command = input()

    if command == "Registration":
        break

    real_command = command.split()
    action = real_command[0]

    if action == "Letters":

        if real_command[1] == "Lower":
            username = username.lower()

        else:
            username = username.upper()

        print(username)

    elif action == "Reverse":
        start_index = int(real_command[1])
        end_index = int(real_command[2])

        if 0 <= start_index <= len(username) and 0 <= end_index <= len(username):
            reversed_substring = username[start_index:end_index + 1][::-1]
            print(reversed_substring)

    elif action == "Substring":
        substring = real_command[1]
        index = username.find(substring)

        if substring in username:
            username = username[:index] + username[index+len(substring):]

            print(username)

        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif action == "Replace":
        replace_char = real_command[1]

        username = username.replace(replace_char, "-")
        print(username)

    elif action == "IsValid":
        char = real_command[1]

        if char in username:
            print("Valid username.")

        else:
            print(f"{char} must be contained in your username.")

