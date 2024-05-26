n = int(input())
matrix = []
alice = []
tea_bags = 0

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
}

for row in range(n):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice = [row, matrix[row].index("A")]
        matrix[alice[0]][alice[1]] = "*"


while tea_bags < 10:
    command = input()

    position = directions[command](alice[0], alice[1])

    if not (0 <= position[0] < n and 0 <= position[1] < n):
        break

    alice = position
    element = matrix[position[0]][position[1]]
    matrix[position[0]][position[1]] = "*"

    if element == "R":
        break
    elif element.isdigit():
        tea_bags += int(element)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[" ".join(row) for row in matrix], sep="\n")
