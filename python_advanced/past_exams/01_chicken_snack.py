from collections import deque

money = [int(x) for x in input().split()]
prices = deque(int(x) for x in input().split())
food_counter = 0

while money and prices:
    c_money = money.pop()
    c_price = prices.popleft()

    if c_price > c_money:
        continue

    if c_money > c_price:
        if money:
            money[-1] += (c_money - c_price)

    food_counter += 1

if food_counter >= 4:
    print(f"Gluttony of the day! Henry ate {food_counter} foods.")
elif not food_counter:
    print("Henry remained hungry. He will try next weekend again.")
elif food_counter == 1:
    print(f"Henry ate: {food_counter} food.")
else:
    print(f"Henry ate: {food_counter} foods.")
