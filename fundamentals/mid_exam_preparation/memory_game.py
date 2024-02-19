def check_matching(index1, index2, elements):
    if elements[index1] == elements[index2]:
        element = elements[index1]
        print(f"Congrats! You have found matching elements - {element}!")
        elements.remove(element)
        elements.remove(element)
        return elements

    elif elements[index1] != elements[index2]:
        print("Try again!")
        return elements


def check_validity(first_index, second_index, moves, elements):
    if first_index == second_index or \
            (not 0 <= first_index < len(elements) or not 0 <= second_index < len(elements)):
        middle = len(elements) // 2
        elements.insert(middle, f"-{moves}a")
        elements.insert(middle, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        return False
    return True


def memory_game(elements):
    moves = 0

    while True:
        command = input()
        if command == "end":
            return f"Sorry you lose :(\n{' '.join(elements)}"

        moves += 1
        explode = command.split()
        first_index = int(explode[0])
        second_index = int(explode[1])

        if check_validity(first_index, second_index, moves, elements):
            check_matching(first_index, second_index, elements)
            if not elements:
                return f"You have won in {moves} turns!"


elements_ = input().split()
print(memory_game(elements_))
