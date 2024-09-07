two_strings = input()
total_sum = 0

first_string, second_string = two_strings.split()

if len(first_string) > len(second_string):
    for char in range(len(second_string)):
        total_sum += ord(first_string[char]) * ord(second_string[char])

    for diff_char in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[diff_char])

elif len(second_string) > len(first_string):
    for char in range(len(first_string)):
        total_sum += ord(second_string[char]) * ord(first_string[char])

    for diff_char in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[diff_char])

else:
    for char in range(len(second_string)):
        total_sum += ord(first_string[char]) * ord(second_string[char])

print(total_sum)
