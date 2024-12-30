from collections import deque
from math import ceil


def print_result(bee_groups, bee_eaters_groups):
    print("The final battle is over!")
    if not bee_groups and not bee_eaters_groups:
        print("But no one made it out alive!")
    elif bee_groups:
        print(f"Bee groups left: {', '.join(map(str, bee_groups))}")
    else:
        print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters_groups))}")

def main():
    bee_groups = deque(int(x) for x in input().split())
    bee_eaters_groups = [int(x) for x in input().split()]

    while bee_eaters_groups and bee_groups:
        bees = bee_groups.popleft()
        bee_eaters = bee_eaters_groups.pop()
        needed_bee_eaters = bees / 7

        if bee_eaters > needed_bee_eaters:
            surviving_bee_eaters = ceil(bee_eaters - needed_bee_eaters)
            bee_eaters_groups.append(surviving_bee_eaters)
        elif bee_eaters < needed_bee_eaters:
            surviving_bees = bees - (bee_eaters * 7)
            bee_groups.append(surviving_bees)

    print_result(bee_groups, bee_eaters_groups)

if __name__ == '__main__':
    main()
    