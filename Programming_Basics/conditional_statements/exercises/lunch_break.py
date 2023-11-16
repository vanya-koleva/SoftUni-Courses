from math import ceil

series_name = (input())
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4

time_left = break_time - lunch_time - relax_time
difference = abs(time_left - episode_time)
difference = ceil(difference)

if time_left >= episode_time:
    print(f"You have enough time to watch {series_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {difference} more minutes.")