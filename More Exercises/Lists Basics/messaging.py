sequence_of_numbers = list(map(int, input().split()))
string_list = list(input())

final_word = ""
for number in sequence_of_numbers:
    number_list = list(map(int, str(number)))
    summed_numbers = sum(number_list)
    difference = summed_numbers - len(string_list)
    if summed_numbers >= len(string_list):
        final_word += string_list[difference]
        string_list.pop(difference)
    else:
        final_word += string_list[summed_numbers]
        string_list.pop(difference)

print(final_word)
