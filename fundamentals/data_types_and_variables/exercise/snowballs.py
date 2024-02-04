number_of_snowballs = int(input())
highest_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
for current_snowball in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight / time_needed) ** quality
    if value > highest_value:
        highest_value = value
        snowball_weight = weight
        snowball_time = time_needed
        snowball_quality = quality

print(f"{snowball_weight} : {snowball_time} = {int(highest_value)} ({snowball_quality})")