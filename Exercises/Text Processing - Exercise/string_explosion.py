text = input()
final_string = ""
strength = 0

for index in range(len(text)):
    if text[index] != ">" and strength > 0:
        strength -= 1

    elif text[index] == ">":
        final_string += text[index]
        strength += int(text[index + 1])

    else:
        final_string += text[index]

print(final_string)
