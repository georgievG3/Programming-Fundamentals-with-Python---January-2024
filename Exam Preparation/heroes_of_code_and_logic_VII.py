number = int(input())
heroes = {}

for line in range(number):
    hero_name, hp, mp = input().split()

    heroes[hero_name] = {"HP": int(hp), "MP": int(mp)}

while True:
    command = input()

    if command == "End":
        break

    real_command = command.split(" - ")
    action = real_command[0]

    if action == "CastSpell":
        name = real_command[1]
        mp_needed = int(real_command[2])
        spell_name = real_command[3]

        if mp_needed <= heroes[name]["MP"]:
            heroes[name]["MP"] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")

        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        name = real_command[1]
        damage = int(real_command[2])
        attacker = real_command[3]

        heroes[name]["HP"] -= damage

        if heroes[name]["HP"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")

        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")

    elif action == "Recharge":
        name = real_command[1]
        amount = int(real_command[2])

        heroes[name]["MP"] += amount

        if heroes[name]["MP"] > 200:
            amount = 200 - (heroes[name]["MP"] - amount)
            heroes[name]["MP"] = 200

        print(f"{name} recharged for {amount} MP!")

    elif action == "Heal":
        name = real_command[1]
        amount = int(real_command[2])

        heroes[name]["HP"] += amount

        if heroes[name]["HP"] > 100:
            amount = 100 - (heroes[name]["HP"] - amount)
            heroes[name]["HP"] = 100


        print(f"{name} healed for {amount} HP!")

for key, value in heroes.items():
    print(f"{key}")
    for k, v in value.items():
        print(f"  {k}: {v}")

