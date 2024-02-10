number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:
    command = input().split()
    if "End" in command:
        print(train)
        break
    elif "add" in command:
        train[-1] += int(command[1])
    elif "insert" in command:
        index = int(command[1])
        train[index] += int(command[2])
    elif "leave" in command:
        index = int(command[1])
        train[index] -= int(command[2])
