phonebook = {}

command = input()
while not command.isdigit():

    name, number = command.split("-")

    if name not in phonebook:
        phonebook[name] = 0
    phonebook[name] = number

    command = input()

for i in range(int(command)):
    phone_name = input()

    if phone_name in phonebook:
        print(f"{phone_name} -> {phonebook.get(phone_name)}")

    else:
        print(f"Contact {phone_name} does not exist.")
