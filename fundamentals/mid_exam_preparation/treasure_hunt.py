def process_steal(initial_list, number):
    cut_part = initial_list[-number:]
    initial_list = initial_list[:-number]
    print(", ".join(cut_part))
    return initial_list


def process_drop(initial_list, idx):
    if idx in range(len(initial_list)):
        item = initial_list.pop(idx)
        initial_list.append(item)
    return initial_list


def process_loot(initial_list, explode_list):
    explode_list = explode_list[1:]
    for item in explode_list:
        if item not in initial_list:
            initial_list.insert(0, item)
    return initial_list


treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    explode = command.split()
    action = explode[0]

    if action == "Loot":
        treasure_chest = process_loot(treasure_chest, explode)

    elif action == "Drop":
        index = int(explode[1])
        treasure_chest = process_drop(treasure_chest, index)

    elif action == "Steal":
        count = int(explode[1])
        treasure_chest = process_steal(treasure_chest, count)

    command = input()

if treasure_chest:
    average_gain = sum(len(x) for x in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
