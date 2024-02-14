from math import floor


def calculate_length(x1, y1, x2, y2):
    result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return result


def calculate_closest_point_to_0(x1, y1, x2, y2):
    distance1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance2 = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance1 <= distance2:
        return (x1, y1), (x2, y2)
    else:
        return (x2, y2), (x1, y1)


def print_longest_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line1_length = calculate_length(x1, y1, x2, y2)
    line2_length = calculate_length(x3, y3, x4, y4)

    if line1_length >= line2_length:
        point1, point2 = calculate_closest_point_to_0(x1, y1, x2, y2)
    else:
        point1, point2 = calculate_closest_point_to_0(x3, y3, x4, y4)

    print(f"({floor(point1[0])}, {floor(point1[1])})({floor(point2[0])}, {floor(point2[1])})")


coordinates = []
for i in range(8):
    point_coordinates = float(input())
    coordinates.append(point_coordinates)
print_longest_line(*coordinates)
