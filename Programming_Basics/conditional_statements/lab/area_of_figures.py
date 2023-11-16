from math import pi

figure = input()
if figure == "square":
    length = float(input())
    area = length * length
elif figure == "rectangle":
    first_length = float(input())
    second_length = float(input())
    area = first_length * second_length
elif figure == "circle":
    radius = float(input())
    #A = π r²
    area = pi * radius ** 2
elif figure == "triangle":
    length = float(input())
    height = float(input())
    #A = 1/2 × b × h
    area = 0.5 * length * height

print(f"{area:.3f}")
