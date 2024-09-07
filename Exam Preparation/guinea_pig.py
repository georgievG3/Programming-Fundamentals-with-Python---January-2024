quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
pig_weight = float(input()) * 1000

is_enough = True
for current_day in range(1, 30 + 1):
    quantity_food -= 300

    if current_day % 2 == 0:
        quantity_hay -= (5 * quantity_food) / 100

    if current_day % 3 == 0:
        quantity_cover -= pig_weight / 3

    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        is_enough = False
        break

excessHay = quantity_hay / 1000
excessFood = quantity_food / 1000
excessCover = quantity_cover / 1000

if is_enough:
    print(f"Everything is fine! Puppy is happy! Food: {excessFood:.2f}, Hay: {excessHay:.2f}, Cover: {excessCover:.2f}.")
else:
    print("Merry must go to the pet store!")
