number_of_cargos = int(input())
price_per_ton = 0
minibus = 0
truck = 0
train = 0
total_tons = 0

for i in range(number_of_cargos):
    tons = int(input())
    total_tons += tons
    if tons <= 3:
        minibus += tons
    elif tons <= 11:
        truck += tons
    else:
        train += tons

total_price = minibus * 200 + truck * 175 + train * 120
average_price = total_price / total_tons
minibus_percentage = minibus / total_tons * 100
truck_percentage = truck / total_tons * 100
train_percentage = train / total_tons * 100

print(f'{average_price:.02f}')
print(f'{minibus_percentage:.02f}%')
print(f'{truck_percentage:.02f}%')
print(f'{train_percentage:.02f}%')
