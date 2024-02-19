def process_shoot(targets_list, ind, power):
    if ind in range(len(targets_list)):
        targets_list[ind] -= power
        if targets_list[ind] <= 0:
            targets_list.pop(ind)
    return targets_list


def process_add(list_of_targets, inx, value):
    if inx in range(len(list_of_targets)):
        list_of_targets.insert(inx, value)
    else:
        print("Invalid placement!")
    return list_of_targets


def process_strike(list_targets, idx, radius):
    if idx + radius in range(len(list_targets)) and idx - radius in range(len(list_targets)):
        list_targets = list_targets[0: idx - radius] + list_targets[idx + radius + 1:]
    else:
        print("Strike missed!")
    return list_targets


def moving_target(targets):
    command = input()
    while command != "End":
        explode = command.split()
        action = explode[0]
        index = int(explode[1])
        number = int(explode[2])

        if action == "Shoot":
            targets = process_shoot(targets, index, number)

        elif action == "Add":
            targets = process_add(targets, index, number)

        else:
            targets = process_strike(targets, index, number)

        command = input()
    return "|".join(str(x) for x in targets)


targets_ = [int(x) for x in input().split()]
print(moving_target(targets_))
