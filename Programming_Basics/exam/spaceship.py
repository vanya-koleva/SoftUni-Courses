from math import floor

width = float(input())
length = float(input())
height = float(input())
average_height_of_astronauts = float(input())

volume_of_one_room = (average_height_of_astronauts +0.4) * 2 * 2
volume_of_the_spaceship = width * length * height
number_of_astronauts = volume_of_the_spaceship / volume_of_one_room
number_of_astronauts = floor(number_of_astronauts)

if 3 <= number_of_astronauts <= 10:
    print(f"The spacecraft holds {number_of_astronauts} astronauts.")
elif number_of_astronauts < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")