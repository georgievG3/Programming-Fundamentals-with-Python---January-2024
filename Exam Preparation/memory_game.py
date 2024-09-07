sequence_of_elements = input().split()

number_of_moves = 0
is_brake = False
while True:
    command = input()

    if command == "end":
        is_brake = True
        break

    index_one, index_two = list(map(int, command.split()))

    if index_one == index_two or index_one < 0 or index_two < 0 or index_one >= len(
            sequence_of_elements) or index_two >= len(sequence_of_elements):
        number_of_moves += 1
        sequence_of_elements.insert(len(sequence_of_elements) // 2, f"-{number_of_moves}a")
        sequence_of_elements.insert(len(sequence_of_elements) // 2, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence_of_elements[index_one] == sequence_of_elements[index_two]:
        number_of_moves += 1
        removed_item = sequence_of_elements[index_one]
        new_list = [item for item in sequence_of_elements if item != sequence_of_elements[index_one]]
        sequence_of_elements = new_list
        print(f"Congrats! You have found matching elements - {removed_item}!")

    elif sequence_of_elements[index_one] != sequence_of_elements[index_two]:
        number_of_moves += 1
        print("Try again!")

    if len(sequence_of_elements) <= 0 and not is_brake:
        print(f"You have won in {number_of_moves} turns!")
        break

if is_brake and sequence_of_elements:
    print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
