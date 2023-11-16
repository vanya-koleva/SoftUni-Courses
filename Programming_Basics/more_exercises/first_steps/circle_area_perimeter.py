from math import pi

radius = float(input())
#A = π r²
area = pi * radius ** 2
# perimeter = 2πr
perimeter = 2 * pi * radius
print(f"{area:.02f}")
print(f"{perimeter:.02f}")
