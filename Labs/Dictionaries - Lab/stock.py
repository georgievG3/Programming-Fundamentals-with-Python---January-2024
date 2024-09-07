elements = input().split()
products = input().split()
elements_dict = {}

for element in range(0, len(elements), 2):
    key = elements[element]
    value = elements[element + 1]
    elements_dict[key] = int(value)

for item in products:
    if item in elements_dict:
        print(f"We have {elements_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
