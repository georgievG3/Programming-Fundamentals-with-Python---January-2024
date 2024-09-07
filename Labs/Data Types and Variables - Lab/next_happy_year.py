year = int(input())

while True:
    year += 1
    is_happy_year = True
    already_found = ""
    for digit in str(year):
        if digit in already_found:
            is_happy_year = False
            break
        already_found += digit
    if is_happy_year:
        break
print(year)
