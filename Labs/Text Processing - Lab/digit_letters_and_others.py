text = input()

digits = ""
letters = ""
other = ""

for letter in text:

    if letter.isdigit():
        digits += letter

    elif letter.isalpha():
        letters += letter

    else:
        other += letter

print(f"{digits}\n{letters}\n{other}")
