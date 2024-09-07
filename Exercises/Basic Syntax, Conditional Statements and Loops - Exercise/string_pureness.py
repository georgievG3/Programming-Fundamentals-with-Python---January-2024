string_count = int(input())

for _ in range(string_count):
    string = input()
    if "," in string:
        print(f"{string} is not pure!")
    elif "." in string:
        print(f"{string} is not pure!")
    elif "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
