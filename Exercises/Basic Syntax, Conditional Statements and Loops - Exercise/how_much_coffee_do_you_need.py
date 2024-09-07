upper_list = ["CODING", "CAT", "DOG", "MOVIE"]
lower_list = ["coding", "cat", "dog", "movie"]

coffee_count = 0
command = input()
while command != "END":
    string = command
    if string in upper_list:
        coffee_count += 2
    elif string in lower_list:
        coffee_count += 1
    else:
        pass

    command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
