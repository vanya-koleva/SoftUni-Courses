inventory = input().split(", ")
command = input()

while command != "Craft!":
    explode = command.split(" - ")
    action = explode[0]
    item = explode[1]

    if action == "Collect":
        if item not in inventory:
            inventory.append(item)

    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)

    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            index = inventory.index(old_item)
            inventory.insert(index + 1, new_item)

    else:
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()

print(", ".join(inventory))
