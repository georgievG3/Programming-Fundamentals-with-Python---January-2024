def characters_between_two(char1, char2):
    result = ""
    for digit in range(ord(char1) + 1, ord(char2)):
        result += chr(digit)

    return result
char1 = input()
char2 = input()
print(" ".join(characters_between_two(char1, char2)))