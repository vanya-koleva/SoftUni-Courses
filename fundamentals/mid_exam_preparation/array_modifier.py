array = [int(x) for x in input().split()]
command = input()

while command != "end":
    explode = command.split()

    if "swap" in explode:
        index1, index2 = int(explode[1]), int(explode[2])
        array[index1], array[index2] = array[index2], array[index1]

    elif "multiply" in explode:
        index1, index2 = int(explode[1]), int(explode[2])
        array[index1] *= array[index2]

    else:
        array = [x -1 for x in array]

    command = input()

print(*array, sep=", ")
