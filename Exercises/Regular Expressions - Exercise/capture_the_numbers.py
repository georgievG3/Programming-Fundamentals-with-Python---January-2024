import re

text = input()
while text:
    pattern = r"\d+"
    matches = re.finditer(pattern, text)

    for match in matches:
        print(match.group(), end=" ")

    text = input()
