first_sequence = input().split(", ")
second_sequence = input().split(", ")
final_list = []

for word in first_sequence:
    for substring in second_sequence:
        if word in substring:
            final_list.append(word)
            break
print(final_list)

# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# print([first_string for first_string in first_sequence if any(first_string in second_string for second_string in second_sequence)])
