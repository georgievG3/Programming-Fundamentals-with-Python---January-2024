import re

text = input()

hidden_words = []
mirror_words = []

hidden_words_pattern = r"(#|@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
matches = re.findall(hidden_words_pattern, text)

for match in matches:
    hidden_words.append([match[1], match[2]])

for hidden_word in hidden_words:
    if hidden_word[0] == hidden_word[1][::-1]:
        mirror_words.append([hidden_word[0], hidden_word[1]])

if hidden_words:
    print(f"{len(hidden_words)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    mirror_string = ""
    for mirror_word in mirror_words:
        mirror_string += f"{mirror_word[0]} <=> {mirror_word[1]}, "
    print(mirror_string[:-2])

else:
    print("No mirror words!")