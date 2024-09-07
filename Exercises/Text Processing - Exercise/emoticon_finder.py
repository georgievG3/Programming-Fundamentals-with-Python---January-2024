text = input().split()

for word in text:
    for i in range(len(word)):
        if word[i] == ":":
            print(f"{word[i]}{word[i + 1]}")