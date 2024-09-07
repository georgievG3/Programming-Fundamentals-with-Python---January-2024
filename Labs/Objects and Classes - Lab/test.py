emails = []

while True:
    command = input()

    if command == "Stop":
        break

    token = command.split()

    sender = token[0]
    receiver = token[1]
    content = token[2]

    email = Email(sender, receiver, content)
    emails.append(email)