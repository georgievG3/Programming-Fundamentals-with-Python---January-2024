text = input().split()

characters_count = {}

for word in text:
    for char in word:
        if char not in characters_count:
            characters_count[char] = 0
        characters_count[char] += 1

for key, value in characters_count.items():
    print(f"{key} -> {value}")