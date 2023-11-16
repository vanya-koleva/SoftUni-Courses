chrysanthemums_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
holiday = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
else:
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

total_price = chrysanthemums_price * chrysanthemums_number + \
              roses_price * roses_number + \
              tulips_price * tulips_number
total_flowers = chrysanthemums_number + roses_number + tulips_number

if holiday == 'Y':
    total_price *= 1.15
if tulips_number > 7 and season == 'Spring':
    total_price *= 0.95
if roses_number >= 10 and season == "Winter":
    total_price *= 0.9
if total_flowers > 20:
    total_price *= 0.8
total_price += 2

print(f'{total_price:.02f}')