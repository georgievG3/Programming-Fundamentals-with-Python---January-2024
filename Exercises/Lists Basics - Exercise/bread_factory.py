working_events = input().split("|")

initial_energy = 100
initial_coins = 100

managed_all_events = True
for working_event in working_events:

    event_info = working_event.split("-")
    event = event_info[0]
    number = int(event_info[1])

    if event == "rest":
        gained_energy = 0

        if initial_energy + number <= 100:
            gained_energy = number
            initial_energy += number
        else:
            gained_energy = 100 - initial_energy
            initial_energy = 100
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {initial_energy}.')

    elif event == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += number
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
            continue

    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            managed_all_events = False
            break

if managed_all_events:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")

