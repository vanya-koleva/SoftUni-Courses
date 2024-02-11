number_of_electrons = int(input())
shells = []

for shell in range(1, number_of_electrons +1):
    maximum_number_of_electrons = 2 * shell ** 2
    if number_of_electrons >= maximum_number_of_electrons:
        shells.append(maximum_number_of_electrons)
        number_of_electrons -= maximum_number_of_electrons
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break

print(shells)
