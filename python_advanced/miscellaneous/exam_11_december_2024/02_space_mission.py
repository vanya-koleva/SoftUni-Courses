def check_boundaries(x, y, num):
    return 0 <= x < num and 0 <= y < num

def initialize_matrix_and_position(n):
    grid = []
    pos = []
    for i in range(n):
        line = input().split()
        grid.append(line)
        if "S" in line:
            pos = [i, grid[i].index("S")]
    return grid, pos


def main():
    n = int(input())
    resources = 100

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1),
    }

    matrix, position = initialize_matrix_and_position(n)
    matrix[position[0]][position[1]] = "."

    while resources >= 5:
        command = input()
        r, c = position[0] + directions[command][0], position[1] + directions[command][1]

        if not check_boundaries(r, c, n):
            print("Mission failed! The spaceship was lost in space.")
            break

        position = [r, c]
        resources -= 5
        el = matrix[r][c]

        if el == "M":
            resources -= 5
            matrix[r][c] = "."
        elif el == "R":
            resources = min(100, resources + 10)
        elif el == "P":
            print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
            break

    else:
        print("Mission failed! The spaceship was stranded in space.")

    if matrix[position[0]][position[1]] != "P":
        matrix[position[0]][position[1]] = "S"

    [print(" ".join(x)) for x in matrix]

if __name__ == '__main__':
    main()
