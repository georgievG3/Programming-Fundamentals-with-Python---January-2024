def contains(raw_key, substring):
    if substring in raw_key:
        print(f"{raw_key} contains {substring}")
    else:
        print("Substring not found!")


def flip(raw_key, command):
    start_index = int(command[2])
    end_index = int(command[3])

    flipped_key = ""
    for i, char in enumerate(raw_key):
        if start_index <= i < end_index:
            if command[1] == "Upper" and char.isalpha():
                char = char.upper()
            elif command[1] == "Lower" and char.isalpha():
                char = char.lower()
        flipped_key += char

    return flipped_key


def slice_key(raw_key, command):
    start_index = int(command[1])
    end_index = int(command[2])

    sliced = raw_key[start_index:end_index]
    raw_key = raw_key.replace(sliced, "", 1)

    return raw_key


raw_key = input()

while True:
    text = input()

    if text == "Generate":
        break

    command = text.split(">>>")

    if command[0] == "Contains":
        contains(raw_key, command[1])

    elif command[0] == "Flip":
        raw_key = flip(raw_key, command)
        print(raw_key)

    elif command[0] == "Slice":
        raw_key = slice_key(raw_key, command)
        print(raw_key)

print(f"Your activation key is: {raw_key}")