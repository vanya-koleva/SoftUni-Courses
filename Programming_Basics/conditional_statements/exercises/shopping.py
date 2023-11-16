budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram_memory = int(input())

total_video_cards_price = number_of_video_cards * 250
one_processor_price = total_video_cards_price * 0.35
total_processors_price = number_of_processors * one_processor_price
one_ram_memory_price = total_video_cards_price * 0.1
total_ram_memory_price = number_of_ram_memory * one_ram_memory_price

total_price = total_video_cards_price + total_processors_price + total_ram_memory_price
if number_of_video_cards > number_of_processors:
    total_price *= 0.85
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {difference:.02f} leva left!")
else:
    print(f"Not enough money! You need {difference:.02f} leva more!")