import re

text = input()
cool_treshold = 1
cool_emojis = []
found_emojis = 0

result = re.findall("\d", text)

for digit in result:
    cool_treshold *= int(digit)


emoji_pattern = r"(\*\*|\::)([A-Z][a-z]{2,})\1"
found_emoji = re.finditer(emoji_pattern, text)

for emoji in found_emoji:
    found_emojis += 1
    treshold = 0

    for char in emoji.group(2):
        treshold += ord(char)

    if treshold >= cool_treshold:
        cool_emojis.append(emoji.group(1) + emoji.group(2) + emoji.group(1))

print(f"Cool threshold: {cool_treshold}\n{found_emojis} emojis found in the text.", end=" ")
print("The cool ones are:")
for cool_emoji in cool_emojis:
    print(cool_emoji)

