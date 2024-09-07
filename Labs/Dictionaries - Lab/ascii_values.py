characters = input().split(", ")

character_dict = {word: ord(word) for word in characters}
print(character_dict)