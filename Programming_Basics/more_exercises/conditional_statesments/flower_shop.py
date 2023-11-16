from math import floor, ceil

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cactuses = int(input())
present_price = float(input())

price_magnolias = 3.25
price_hyacinths = 4
price_roses = 3.5
price_cactuses = 8

#От общата сума, Мария трябва да плати 5% данъци.

total_magnolias = number_of_magnolias * price_magnolias
total_hyacinths = number_of_hyacinths * price_hyacinths
total_roses = number_of_roses * price_roses
total_cactuses = number_of_cactuses * price_cactuses
total_sum = total_magnolias + total_hyacinths + total_roses + total_cactuses
total_sum = total_sum - total_sum * 0.05
difference = abs(total_sum - present_price)

if total_sum >= present_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")