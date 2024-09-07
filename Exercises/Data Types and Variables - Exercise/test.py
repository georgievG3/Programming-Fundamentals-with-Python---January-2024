group_size = int(input())
days = int(input())

coins = 0

for day in range(1, days + 1):
    coins += 50
    coins -= 2 * group_size
    if day % 10 == 0:
        group_size -= 2
        continue
    elif day % 15 == 0:
        group_size += 5
    elif day % 5 == 0 and day % 3 == 0:
        coins += 20 * group_size
        coins -= 2 * group_size
    elif day % 3 == 0:
        coins -= 3 * group_size
    elif day % 5 == 0:
        coins += 20 * group_size


total_coins = coins / group_size
print(f"{group_size} companions received {round(total_coins)} coins each.")
