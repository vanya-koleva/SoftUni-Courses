x_height_of_the_house = float(input())
y_lenght_of_side_wall = float(input())
h_height_of_triangle_wall = float(input())

side_wall = x_height_of_the_house * y_lenght_of_side_wall
window = 1.5 * 1.5
total_side_walls = side_wall * 2 - window * 2
back_wall = x_height_of_the_house * x_height_of_the_house
door = 1.2 * 2
total_front_back_walls = back_wall * 2 - door
total_house = total_side_walls + total_front_back_walls
green_paint = total_house / 3.4
print(f"{green_paint:.02f}")

roof_rectangles = 2 * x_height_of_the_house * y_lenght_of_side_wall
#A = 1/2 × b × h
roof_triangles = 2 * (0.5 * x_height_of_the_house * h_height_of_triangle_wall)
total_roof = roof_rectangles + roof_triangles
red_paint = total_roof / 4.3
print(f"{red_paint:.02f}")