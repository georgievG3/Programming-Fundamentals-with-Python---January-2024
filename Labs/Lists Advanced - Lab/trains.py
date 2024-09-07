number_of_wagons = int(input())
wagons_people = [0] * number_of_wagons

command = input()

while command != "End":
    command_list = command.split()
    people = int(command_list[-1])
    instruction = command_list[0]
    index = int(command_list[1])
    if instruction == "add":
        wagons_people[-1] += people
    elif instruction == "insert":
        wagons_people[index] += people
    elif instruction == "leave":
        wagons_people[index] -= people

    command = input()

print(wagons_people)