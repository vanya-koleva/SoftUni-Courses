def check_boundaries(x, y, num):
    return 0 <= x < num and 0 <= y < num

def main():
    n = int(input())
    matrix = []
    position = []
    stars = 2

    mapper = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1),
    }

    for i in range(n):
        line = input().split()
        matrix.append(line)
        if "P" in line:
            position = [i, matrix[i].index("P")]
            matrix[position[0]][position[1]] = "."

    while 0 < stars < 10:
        command = input()
        r, c = position[0] + mapper[command][0], position[1] + mapper[command][1]

        if not check_boundaries(r, c, n):
            r, c = 0, 0

        el = matrix[r][c]

        if el == "*":
            stars += 1
            matrix[r][c] = "."
        elif el == "#":
            stars -= 1
            continue

        position = [r, c]

    matrix[position[0]][position[1]] = "P"

    if stars == 10:
        print("You won! You have collected 10 stars.")
    elif stars == 0:
        print("Game over! You are out of any stars.")

    print(f"Your final position is {position}")

    [print(" ".join(x)) for x in matrix]

if __name__ == '__main__':
    main()