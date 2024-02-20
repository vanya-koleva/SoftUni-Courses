def shopping_list(list_of_groceries):
    command = input()
    while command != "Go Shopping!":
        explode = command.split()
        action, item = explode[0], explode[1]

        if action == "Urgent":
            if item not in list_of_groceries:
                list_of_groceries.insert(0, item)

        elif action == "Unnecessary":
            if item in list_of_groceries:
                list_of_groceries.remove(item)

        elif action == "Correct":
            old_item, new_item = item, explode[2]
            if old_item in list_of_groceries:
                index = list_of_groceries.index(old_item)
                list_of_groceries[index] = new_item

        elif action == "Rearrange":
            if item in list_of_groceries:
                list_of_groceries.remove(item)
                list_of_groceries.append(item)

        command = input()

    return ", ".join(list_of_groceries)


groceries = input().split("!")
print(shopping_list(groceries))
