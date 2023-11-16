number_of_clients = int(input())
total_money = 0

for _ in range(number_of_clients):
    number_of_purchases = 0
    sum_per_client = 0
    purchase = input()
    while purchase != "Finish":
        number_of_purchases += 1
        if purchase == "basket":
            price = 1.5
        elif purchase == "wreath":
            price = 3.8
        else:
            price = 7
        sum_per_client += price
        purchase = input()
    else:
        if number_of_purchases % 2 == 0:
            sum_per_client *= 0.8
        print(f"You purchased {number_of_purchases} items for {sum_per_client:.2f} leva.")
        total_money += sum_per_client

average = total_money / number_of_clients
print(f"Average bill per client is: {average:.2f} leva.")