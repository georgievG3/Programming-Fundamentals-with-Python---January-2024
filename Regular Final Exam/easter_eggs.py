import re

text = input()
pattern = r"((\@|\#){1,}([a-z]{3,})(\@|\#){1,})([^a-zA-Z\d]*?)((\/{1,})(\d+)(\/{1,}))"
matches = re.findall(pattern, text)

for match in matches:
    print(f"You found {match[7]} {match[2]} eggs!")