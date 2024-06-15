n = int(input())
matrix = []
position = []
money = 100
won = False
lost = False

for i in range(n):
    line = list(input())
    matrix.append(line)
    if "G" in line:
        position = [i, matrix[i].index("G")]
        matrix[i][position[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    if command == "end":
        break

    r, c = position[0] + directions[command][0], position[1] + directions[command][1]
    position = [r, c]

    if not 0 <= r < n and 0 <= c < n:
        lost = True
        break

    element = matrix[r][c]
    matrix[r][c] = "-"

    if element == "W":
        money += 100
    elif element == "P":
        money -= 200
    elif element == "J":
        money += 100000
        won = True
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        break

    if money <= 0:
        money = 0
        lost = True
        break

matrix[position[0]][position[1]] = "G"

if lost:
    print("Game over! You lost everything!")
elif not won:
    print(f"End of the game. Total amount: {money}$")

if money:
    [print("".join(r)) for r in matrix]
