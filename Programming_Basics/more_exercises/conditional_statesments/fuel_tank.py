type_of_fuel = input()
liters_in_tank = float(input())
valid = True

if type_of_fuel == "Diesel":
    type_of_fuel = 'diesel'
elif type_of_fuel == "Gasoline":
    type_of_fuel = 'gasoline'
elif type_of_fuel == "Gas":
    type_of_fuel = 'gas'
else:
    valid = False
if valid == True:
    if liters_in_tank >= 25:
        print(f'You have enough {type_of_fuel}.')
    else:
        print(f'Fill your tank with {type_of_fuel}!')
else:
    print("Invalid fuel!")