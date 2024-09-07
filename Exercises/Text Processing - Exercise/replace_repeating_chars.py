text = input()
new_text = ""
last_char = ""

for char in text:
    if char != last_char:
        new_text += char
        last_char = char

print(new_text)