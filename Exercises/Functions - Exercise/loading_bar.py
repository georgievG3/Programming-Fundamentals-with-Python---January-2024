def loading_bar(number):
    loading_bar_list = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    if int(number) == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    for index in range(0, int(number[0])):
        loading_bar_list[index] = "%"
    return f"{number}% [{''.join(loading_bar_list)}]\nStill loading..."


integer = input()
print(loading_bar(integer))