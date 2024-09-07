number = int(input())

parking = {}

for n in range(number):
    elements = input().split()
    command = elements[0]
    username = elements[1]


    if command == "register":
        plate_number = elements[2]
        if username not in parking:
            parking[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    elif command == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(f"{username}")
            print(f"{username} unregistered successfully")

for name, plate in parking.items():
    print(f"{name} => {plate}")