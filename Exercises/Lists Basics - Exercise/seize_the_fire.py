fire_info = input().split("#")
water = int(input())

effort = 0
total_fire = 0
put_out_cells = []

for fire in fire_info:

    fire_list = fire.split()

    fire_type = fire_list[0]
    cell_value = int(fire_list[2])

    if water < cell_value:
        continue

    if water < 0:
        break

    if fire_type == "High" and 81 <= cell_value <= 125:
        put_out_cells.append(cell_value)
        water -= cell_value
        total_fire += cell_value
        effort += cell_value * 0.25

    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        put_out_cells.append(cell_value)
        water -= cell_value
        total_fire += cell_value
        effort += cell_value * 0.25

    elif fire_type == "Low" and 1 <= cell_value <= 50:
        put_out_cells.append(cell_value)
        water -= cell_value
        total_fire += cell_value
        effort += cell_value * 0.25

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
