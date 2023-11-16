age = int(input())
laundry_price = float(input())
price_per_toy = int(input())
number_of_toys = 0
sum_of_money = 0
total_birthday_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        sum_of_money += 10
        total_birthday_money += sum_of_money - 1
    else:
        number_of_toys += 1
total_toys = number_of_toys * price_per_toy
total_sum = total_toys + total_birthday_money
difference = abs(total_sum - laundry_price)
if total_sum >= laundry_price:
    print(f'Yes! {difference:.02f}')
else:
    print(f'No! {difference:.02f}')