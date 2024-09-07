initial_energy = int(input())
won_battles_count = 0

enough_energy_left = True
while True:
    command = input()

    if command == "End of battle":
        break
    else:
        distance = int(command)

    if initial_energy >= distance:
        initial_energy -= distance
        won_battles_count += 1
        if won_battles_count % 3 == 0:
            initial_energy += won_battles_count
    else:
        print(f"Not enough energy! Game ends with {won_battles_count} won battles and {initial_energy} energy")
        enough_energy_left = False
        break

if enough_energy_left:
    print(f"Won battles: {won_battles_count}. Energy left: {initial_energy}")
