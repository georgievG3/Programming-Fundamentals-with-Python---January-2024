def drive(split_command, owned_cars_dict):
    car_name = split_command[1]
    distance_driven = int(split_command[2])
    given_fuel = int(split_command[3])

    if given_fuel > owned_cars_dict[car_name]["fuel"]:
        print("Not enough fuel to make that ride")

    else:
        owned_cars_dict[car_name]["mileage"] += distance_driven
        owned_cars_dict[car_name]["fuel"] -= given_fuel

        print(f"{car_name} driven for {distance_driven} kilometers. {given_fuel} liters of fuel consumed.")

    if owned_cars_dict[car_name]["mileage"] >= 100000:
        del owned_cars_dict[car_name]

        print(f"Time to sell the {car_name}!")

    return owned_cars_dict

def refuel(split_command, owned_cars_dict):
    car_name = split_command[1]
    given_fuel = int(split_command[2])

    owned_cars_dict[car_name]["fuel"] += given_fuel

    refueled_amount = given_fuel
    if owned_cars_dict[car_name]["fuel"] > 75:
        refueled_amount = 75 - (owned_cars_dict[car_name]["fuel"] - given_fuel)
        owned_cars_dict[car_name]["fuel"] = 75

    print(f"{car_name} refueled with {refueled_amount} liters")

    return owned_cars_dict

def revert(split_command, owned_cars_dict):
    car_name = split_command[1]
    kilometers = int(split_command[2])

    owned_cars_dict[car_name]["mileage"] -= kilometers

    if owned_cars_dict[car_name]["mileage"] < 10000:
        owned_cars_dict[car_name]["mileage"] = 10000

    else:
        print(f"{car_name} mileage decreased by {kilometers} kilometers")

    return owned_cars_dict


number = int(input())

owned_cars = {}

for n in range(number):
    car, mileage, fuel = input().split("|")

    owned_cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

while True:
    command = input()

    if command == "Stop":
        break

    actual_command = command.split(" : ")
    action = actual_command[0]

    if action == "Drive":
        drive(actual_command, owned_cars)

    elif action == "Refuel":
        refuel(actual_command, owned_cars)

    elif action == "Revert":
        revert(actual_command, owned_cars)

for owned_car, owned_car_specs in owned_cars.items():
    print(f"{owned_car} -> Mileage: {owned_car_specs['mileage']} kms, Fuel in the tank: {owned_car_specs['fuel']} lt.")
