some_string = input().split()
total_sum = 0
current_number = ""

for string in some_string:
    first_letter = string[0]
    last_letter = string[-1]

    for char in string:
        if char.isdigit():
            current_number += char

    if first_letter.isupper():
        total_sum += int(current_number) / (ord(first_letter) - 64)

    if first_letter.islower():
        total_sum += int(current_number) * (ord(first_letter) - 96)

    if last_letter.isupper():
        total_sum -= ord(last_letter) - 64

    if last_letter.islower():
        total_sum += ord(last_letter) - 96

    current_number = ""

print(f"{total_sum:.2f}")

