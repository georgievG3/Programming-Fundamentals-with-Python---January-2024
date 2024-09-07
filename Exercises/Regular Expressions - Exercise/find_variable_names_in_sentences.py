import re

pattern = r"\b\_([a-zA-Z]+\b)"
text = input()
matches = re.findall(pattern, text)

print(",".join(matches))