number_of_electrons = int(input())
filled_shells_list = []

for shell in range(1, number_of_electrons + 1):
    electrons_in_shell = 2 * shell ** 2
    if electrons_in_shell <= number_of_electrons:
        filled_shells_list.append(electrons_in_shell)
        number_of_electrons -= electrons_in_shell
    else:
        filled_shells_list.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
    if number_of_electrons <= 0:
        break
print(filled_shells_list)
