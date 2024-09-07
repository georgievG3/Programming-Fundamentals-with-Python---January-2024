sequence_of_numbers = list(map(int, input().split(", ")))

biggest_number = max(sequence_of_numbers)
lowest_number = 0

if biggest_number % 10 != 0:
    biggest_rounded_number = round((biggest_number + 5) / 10) * 10
else:
    biggest_rounded_number = biggest_number

for group in range(10, biggest_rounded_number + 1, 10):
    sorted_list = [number for number in sequence_of_numbers if lowest_number < number <= group]
    lowest_number += 10
    print(f"Group of {group}'s: {sorted_list}")
    sorted_list.clear()
    #
    # numbers = [int(number) for number in input().split(", ")]
    # current_group = 10
    # while numbers:
    #     filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
    #     print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    #     current_group += 10
    #     numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]