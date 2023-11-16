count_of_groups = int(input())
musala_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for i in range(count_of_groups):
    number_of_people = int(input())
    if number_of_people <= 5:
        musala_climbers += number_of_people
    elif number_of_people < 13:
        mont_blanc_climbers += number_of_people
    elif number_of_people < 26:
        kilimanjaro_climbers += number_of_people
    elif number_of_people < 41:
        k2_climbers += number_of_people
    else:
        everest_climbers += number_of_people
    total_climbers += number_of_people

musala_climbers_percentage = musala_climbers / total_climbers * 100
mont_blanc_climbers_percentage = mont_blanc_climbers / total_climbers * 100
kilimanjaro_climbers_percentage = kilimanjaro_climbers/ total_climbers * 100
k2_climbers_percentage = k2_climbers / total_climbers * 100
everest_climbers_percentage = everest_climbers / total_climbers * 100

print(f'{musala_climbers_percentage:.02f}%')
print(f'{mont_blanc_climbers_percentage:.02f}%')
print(f'{kilimanjaro_climbers_percentage:.02f}%')
print(f'{k2_climbers_percentage:.02f}%')
print(f'{everest_climbers_percentage:.02f}%')
