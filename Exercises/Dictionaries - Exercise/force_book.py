force_sides_dict = {}
unique_force_users = []
while True:
    command = input()

    if command == "Lumpawaroo":
        break

    split_data_bybar = command.split(" | ")

    if len(split_data_bybar) > 1:
        force_side = split_data_bybar[0]
        force_user = split_data_bybar[1]

        if force_user not in unique_force_users:
            if force_side not in force_sides_dict:
                force_sides_dict[force_side] = []
            if force_user not in force_sides_dict[force_side]:
                force_sides_dict[force_side].append(force_user)
                unique_force_users.append(force_user)

    elif len(split_data_bybar) == 1:
        split_data_byarrow = command.split(" -> ")
        force_side = split_data_byarrow[1]
        force_user = split_data_byarrow[0]

        if force_side not in force_sides_dict:
            force_sides_dict[force_side] = []
        for side, users in force_sides_dict.items():
            if force_user in users:
                force_sides_dict[side].remove(force_user)
        force_sides_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for sides, members in force_sides_dict.items():
    if members:
        print(f"Side: {sides}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")