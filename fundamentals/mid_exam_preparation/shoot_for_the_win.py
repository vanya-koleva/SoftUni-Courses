def manipulate_values(list_of_targets, index):
    target_value = list_of_targets[index]
    list_of_targets[index] = -1

    for i in range(len(list_of_targets)):
        if list_of_targets[i] == -1:
            continue

        if list_of_targets[i] > target_value:
            list_of_targets[i] -= target_value
        else:
            list_of_targets[i] += target_value

    return list_of_targets


def shoot_for_the_win(list_of_targets):
    count_of_shot_targets = 0
    while True:
        command = input()

        if command == "End":
            break

        index = int(command)

        if 0 <= index < len(list_of_targets) and list_of_targets[index] != -1:
            count_of_shot_targets += 1
            manipulate_values(list_of_targets, index)

    targets_as_string = " ".join(map(str, list_of_targets))
    print(f"Shot targets: {count_of_shot_targets} -> {targets_as_string}")


targets = [int(x) for x in input().split()]
shoot_for_the_win(targets)
