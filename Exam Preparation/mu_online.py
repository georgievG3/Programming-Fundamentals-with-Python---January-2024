dungeon_rooms = input().split("|")

health = 100
bitcoins = 0
room_count = 1

all_rooms_searched = True
for room in dungeon_rooms:
    command, number = [x for x in room.split()]

    if command == "potion":
        old_health = health
        health += int(number)
        if health <= 100:
            print(f"You healed for {int(number)} hp.")
        else:
            healed_amount = 100 - old_health
            health = 100
            print(f"You healed for {healed_amount} hp.")

        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += int(number)
        print(f"You found {number} bitcoins.")

    else:
        health -= int(number)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            all_rooms_searched = False
            break
    room_count += 1

if all_rooms_searched:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")

