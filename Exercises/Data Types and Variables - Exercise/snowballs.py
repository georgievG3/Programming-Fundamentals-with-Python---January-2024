snowballs_made = int(input())

highest_value = 0
highest_weight = 0
highest_time = 0
highest_quality = 0
for snowballs in range(snowballs_made):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = (weight / time_needed) ** quality
    if snowball_value > highest_value:
        highest_value = int(snowball_value)
        highest_weight = weight
        highest_time = time_needed
        highest_quality = quality
print(f"{highest_weight} : {highest_time} = {highest_value} ({highest_quality})")
