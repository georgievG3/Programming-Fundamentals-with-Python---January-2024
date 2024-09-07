while True:
    string = ""
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for character in command:
        string += character*2

    print(string)
