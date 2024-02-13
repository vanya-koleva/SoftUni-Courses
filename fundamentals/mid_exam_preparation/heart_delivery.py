def process_current_house(list_of_neighborhood, current_index):
    hearts_per_jump = 2
    if list_of_neighborhood[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        list_of_neighborhood[current_index] -= hearts_per_jump
        if list_of_neighborhood[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")


def print_result(list_of_neighborhood, last_position):
    print(f"Cupid's last position was {last_position}.")

    if sum(list_of_neighborhood) != 0:
        houses = [x for x in list_of_neighborhood if x != 0]
        house_count = len(houses)
        print(f"Cupid has failed {house_count} places.")
    else:
        print("Mission was successful.")


def heart_delivery(list_of_neighborhood):
    current_index = 0

    while True:
        command = input()

        if command == "Love!":
            break

        jump_length = int(command.split()[1])

        if current_index + jump_length <= len(list_of_neighborhood) -1:
            current_index += jump_length
            process_current_house(list_of_neighborhood, current_index)

        else:
            current_index = 0
            process_current_house(list_of_neighborhood, current_index)

    return list_of_neighborhood, current_index


neighborhood = [int(x) for x in input().split("@")]
neighborhood_condition, last_index = heart_delivery(neighborhood)
print_result(neighborhood_condition, last_index)
