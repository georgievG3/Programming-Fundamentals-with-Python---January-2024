# current_version = input().split(".")
# current_version_number = "".join(current_version)
# next_version = int(current_version_number) + 1
# next_version_as_string = ".".join(str(next_version))
# print(next_version_as_string)

# --------------------------------------

# current_version = list(map(int, input().split(".")))
#
# first_number = current_version[0]
# second_number = current_version[1]
# last_number = current_version[-1]
#
# last_number += 1
#
# if last_number >= 10:
#     last_number -= 10
#     second_number += 1
#     if second_number >= 10:
#         second_number -= 10
#         first_number += 1
#
# print(f"{first_number}.{second_number}.{last_number}")

# ------------------------------------------------

version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) -1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index -1] += 1
print(".".join(str(digit) for digit in version))
