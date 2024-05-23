def swap_elements(indices):
    row1, col1, row2, col2 = indices
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]


def validate_indices(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def validate_input(command_type, indices):
    if len(indices) == 4 and validate_indices(indices) and command_type == "swap":
        return True
    return False


def display_results():
    if validate_input(command, coordinates):
        swap_elements(coordinates)
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    display_results()
