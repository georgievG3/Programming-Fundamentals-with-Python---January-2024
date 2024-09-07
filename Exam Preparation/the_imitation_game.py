encrypted_message = input()

while True:
    command = input()

    if command == "Decode":
        break

    instructions = command.split("|")
    instruction = instructions[0]

    if instruction == "Move":
        number_of_letters = int(instructions[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    elif instruction == "Insert":
        index = int(instructions[1])
        value = instructions[2]

        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif instruction == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]

        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")
