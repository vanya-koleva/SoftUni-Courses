chicken_price = 10.35
fish_price = 12.40
vegetarian_price = 8.15
delivery = 2.50

number_of_chicken = int(input())
number_of_fish = int(input())
number_of_vegetarian = int(input())

total_chicken = number_of_chicken * chicken_price
total_fish = number_of_fish * fish_price
total_vegetarian = number_of_vegetarian * vegetarian_price
total_price = total_chicken + total_fish + total_vegetarian
dessert_price = total_price * 0.2
total_price = total_price + dessert_price + delivery
print(total_price)