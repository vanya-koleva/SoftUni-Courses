country = input()
equipment = input()
grade = 0

if country == 'Russia':
    if equipment == "ribbon":
        grade = 9.100 + 9.400
    elif equipment == 'hoop':
        grade = 9.3 + 9.8
    else:
        grade = 9.6 + 9
elif country == "Bulgaria":
    if equipment == "ribbon":
        grade = 9.600 + 9.400
    elif equipment == 'hoop':
        grade = 9.55 + 9.75
    else:
        grade = 9.5 + 9.4
else:
    if equipment == "ribbon":
        grade = 9.200 + 9.500
    elif equipment == 'hoop':
        grade = 9.45 + 9.35
    else:
        grade = 9.7 + 9.15

difference = abs(20 - grade)
percentage = difference / 20 * 100

print(f"The team of {country} get {grade:.3f} on {equipment}.")
print(f"{percentage:.2f}%")