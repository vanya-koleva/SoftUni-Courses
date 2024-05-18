# elements = {el for _ in range(int(input())) for el in input().split()}

elements = set()

for _ in range(int(input())):
    for el in input().split():
        elements.add(el)

print(*elements, sep="\n")
