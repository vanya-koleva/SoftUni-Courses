from math import ceil

price_of_other_components = 1000
price_per_video_card = int(input())
price_per_jumper = int(input())
price_electricity_per_card_per_day = float(input())
income_per_card_per_day = float(input())

total_video_cards_price = price_per_video_card * 13
total_jumpers_price = price_per_jumper * 13
total_sum = price_of_other_components + total_video_cards_price + total_jumpers_price
income_per_card_per_day -= price_electricity_per_card_per_day
total_income_per_day = 13 * income_per_card_per_day
days = total_sum / total_income_per_day

print(total_sum)
print(ceil(days))

