legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

data = input().split()

is_obtained = False

while not is_obtained:
    for index in range(0, len(data) - 1, 2):
        if not is_obtained:
            quantity = int(data[index])
            material = data[index + 1].lower()

            if material in key_materials:
                key_materials[material] += quantity
                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    is_obtained = True
                    print(f"{legendary_items[material]} obtained!")
            else:
                if material not in junk:
                    junk[material] = 0
                junk[material] += quantity
    if not is_obtained:
        data = input().split()

for mat, quant in key_materials.items():
    print(f"{mat}: {quant}")

for mat, quant in junk.items():
    print(f"{mat}: {quant}")