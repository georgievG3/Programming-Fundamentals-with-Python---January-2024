text = input()
encrypted_version = ""

for char in text:
    char_number = ord(char)
    new_number = char_number + 3

    encrypted_version += chr(new_number)

print(encrypted_version)