number = int(input())
plants_dict = {}

for n in range(number):
    plant, rarity = input().split("<->")

    if plant not in plants_dict:
        plants_dict[plant] = {"rarity": int(rarity), "rating": []}
    plants_dict[plant]["rarity"] = int(rarity)

while True:
    command = input()

    if command == "Exhibition":
        break

    actual_command = command.split(": ")
    action = actual_command[0]

    if action == "Rate":
        plant, rating = actual_command[1].split(" - ")

        if plant not in plants_dict:
            print("error")

        else:
            plants_dict[plant]["rating"].append(int(rating))

    elif action == "Update":
        plant, new_rarity = actual_command[1].split(" - ")

        if plant not in plants_dict:
            print("error")

        else:
            plants_dict[plant]["rarity"] = int(new_rarity)

    elif action == "Reset":
        plant = actual_command[1]

        if plant not in plants_dict:
            print("error")
        else:
            plants_dict[plant]["rating"].clear()

print("Plants for the exhibition:")
for plant_name, plant_info in plants_dict.items():
    if plant_info['rating']:
        print(f"- {plant_name}; Rarity: {plant_info['rarity']}; Rating: {sum(plant_info['rating']) / len(plant_info['rating']):.2f}")
    else:
        print(f"- {plant_name}; Rarity: {plant_info['rarity']}; Rating: {sum(plant_info['rating']):.2f}")