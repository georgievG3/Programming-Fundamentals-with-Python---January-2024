password = input()

while True:
    command = input()

    if command == "Complete":
        break

    real_command = command.split()
    action = real_command[0]

    if action == "Make" and real_command[1] == "Upper":
        index = int(real_command[2])

        if index in range(len(password)):

            upper_letter = password[index].upper()
            password = password[:index] + upper_letter + password[index + 1:]

            print(password)

    elif action == "Make" and real_command[1] == "Lower":
        index = int(real_command[2])

        if index in range(len(password)):

            lower_letter = password[index].lower()
            password = password[:index] + lower_letter + password[index + 1:]

            print(password)

    elif action == "Insert":
        index = int(real_command[1])
        insert_char = real_command[2]

        if index in range(len(password)):
            password = password[:index] + insert_char + password[index:]

            print(password)

    elif action == "Replace":
        replace_char = real_command[1]
        value = int(real_command[2])

        summed_value = ord(replace_char) + value

        if replace_char in password:
            password = password.replace(replace_char, chr(summed_value))

            print(password)

    elif action == "Validation":

        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        if not password.isalnum() and "_" not in password:
            print("Password must consist only of letters, digits and _!")

        if not any(char.isupper() for char in password):
            print("Password must consist at least one uppercase letter!")

        if not any(char.islower() for char in password):
            print("Password must consist at least one lowercase letter!")

        if not any(char.isdigit() for char in password):
            print("Password must consist at least one digit!")

