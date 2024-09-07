target_cities = {}

while True:
    command = input()

    if command == "Sail":
        break

    city_name, population, gold = command.split("||")

    population = int(population)
    gold = int(gold)

    if city_name not in target_cities:
        target_cities[city_name] = []
        target_cities[city_name].append(population)
        target_cities[city_name].append(gold)

    else:
        target_cities[city_name][0] += population
        target_cities[city_name][1] += gold

while True:
    command = input()

    if command == "End":
        break

    actions = command.split("=>")
    action = actions[0]

    if action == "Plunder":
        town = actions[1]
        killed_people = int(actions[2])
        stolen_gold = int(actions[3])

        target_cities[town][0] -= killed_people
        target_cities[town][1] -= stolen_gold

        print(f"{town} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.")

        if target_cities[town][0] <= 0 or target_cities[town][1] <= 0:
            del target_cities[town]
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        town = actions[1]
        gold = int(actions[2])

        if gold >= 0:
            target_cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {target_cities[town][1]} gold.")

        else:
            print("Gold added cannot be a negative number!")

if target_cities:
    print(f"Ahoy, Captain! There are {len(target_cities)} wealthy settlements to go to:")

    for key, value in target_cities.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
