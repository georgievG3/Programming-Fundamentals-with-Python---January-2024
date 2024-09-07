initial_array_values = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "end":
        break

    elif command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_array_values[index1], initial_array_values[index2] = initial_array_values[index2], initial_array_values[index1]

    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_array_values[index1] *= initial_array_values[index2]

    elif command[0] == "decrease":
        initial_array_values = [number - 1 for number in initial_array_values]

print(', '.join(list(map(str, initial_array_values))))
