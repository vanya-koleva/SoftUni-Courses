from collections import deque


def process_queue(names, liters):
    while True:
        command = input().split()
        if "End" in command:
            return liters

        elif "refill" in command:
            liters += int(command[1])

        else:
            requested_liters = int(command[0])
            name = names.popleft()
            if liters >= requested_liters:
                print(f"{name} got water")
                liters -= requested_liters
            else:
                print(f"{name} must wait")


def get_a_queue(names):
    while True:
        name = input()
        if name == "Start":
            return names
        names.append(name)


water = int(input())
people = deque()
people = get_a_queue(people)
water = process_queue(people, water)
print(f"{water} liters left")
