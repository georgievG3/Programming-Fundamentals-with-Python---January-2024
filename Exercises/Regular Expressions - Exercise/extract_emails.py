import re

text = input()
pattern = r"\s(([a-z][a-z0-9\.\-\_]+)@([a-z][a-z\-]+)\.([a-z\.]+)\b)"
matches = re.findall(pattern, text)

for match in matches:
    print(match[0])