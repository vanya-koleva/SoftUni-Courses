number_of_locations = int(input())

for location in range(number_of_locations):
    expected_average_gold = float(input())
    number_of_days = int(input())
    gold_per_location = 0
    for day in range(number_of_days):
        gold_for_the_day = float(input())
        gold_per_location += gold_for_the_day
    average_gold = gold_per_location / number_of_days
    difference = abs(expected_average_gold - average_gold)
    if average_gold >= expected_average_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")