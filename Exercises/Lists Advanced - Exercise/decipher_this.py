def deciphering(message):
    deciphered_message = []
    for word in secret_message:
        new_word = ""
        digits = [i for i in list(word) if i.isdigit()]
        digits_as_string = "".join(digits)
        new_word += chr(int(digits_as_string))
        letter = [i for i in list(word) if i.isalpha()]
        letter[0], letter[-1] = letter[-1], letter[0]
        letters = "".join(letter)
        new_word += letters
        deciphered_message.append(new_word)

    print(" ".join(deciphered_message))

secret_message = input().split()
deciphering(secret_message)
