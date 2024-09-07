def collect_item(element, inventory):
    if element not in inventory:
        inventory.append(element)


def drop_item(element, inventory):
    if element in inventory:
        inventory.remove(element)


def combine_items(old_element, new_element, inventory):

    if old_element in inventory:
        old_el_position = inventory.index(old_element)
        inventory.insert(old_el_position + 1, new_element)


def renew_item(element, inventory):
    if element in inventory:
        inventory.remove(element)
        inventory.append(element)


items_inventory = input().split(", ")

while True:
    command = input()

    if command == "Craft!":
        break

    real_command = command.split(" - ")
    action = real_command[0]

    if action == "Collect":
        item = real_command[1]

        collect_item(item, items_inventory)

    elif action == "Drop":
        item = real_command[1]

        drop_item(item, items_inventory)

    elif action == "Combine Items":
        old_item, new_item = real_command[1].split(":")

        combine_items(old_item, new_item, items_inventory)

    elif action == "Renew":
        item = real_command[1]

        renew_item(item, items_inventory)

print(", ".join(items_inventory))
