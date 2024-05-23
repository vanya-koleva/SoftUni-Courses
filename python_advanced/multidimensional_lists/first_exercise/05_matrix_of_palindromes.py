rows, cols = [int(x) for x in input().split()]

start = ord("a")

for i in range(start, start + rows):
    for j in range(i, i + cols):
        print(chr(i), chr(j), chr(i), sep="", end=" ")

    print()
