lines = int(input())

sum_of_letters = 0
for letters in range(lines):
    letter = input()
    sum_of_letters += ord(letter)
print(f"The sum equals: {sum_of_letters}")
