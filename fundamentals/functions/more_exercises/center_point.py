from math import floor


def calculate_closest_point(x1, y1, x2, y2):
    # distance = sqrt(x ** 2 + y ** 2)
    distance1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance2 = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance1 <= distance2:
        print(f"({floor(x1)}, {floor(y1)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})")


first_point_x = float(input())
first_point_y = float(input())
second_point_x = float(input())
second_point_y = float(input())
calculate_closest_point(first_point_x, first_point_y, second_point_x, second_point_y)
