CAPACITY = 255

lines = int(input())
water_filled = 0
for litres in range(lines):
    litres_of_water = int(input())
    water_filled += litres_of_water
    if water_filled > CAPACITY:
        print("Insufficient capacity!")
        water_filled -= litres_of_water
print(water_filled)
