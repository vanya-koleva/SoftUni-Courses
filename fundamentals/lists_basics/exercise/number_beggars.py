money_offers = input().split(", ")
money_offers_as_int = []
for money in money_offers:
    money_offers_as_int.append(int(money))
number_of_beggars = int(input())
starting_index = 0
sums = []

for beggar in range(number_of_beggars):
    total_sum = 0
    for index in range(starting_index, len(money_offers_as_int), number_of_beggars):
        total_sum += money_offers_as_int[index]
    sums.append(total_sum)
    starting_index += 1

print(sums)
