from collections import deque

time_per_task = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while time_per_task and number_of_tasks:
    current_time = time_per_task.popleft()
    task = number_of_tasks.pop()
    total_time = current_time * task

    if 0 < total_time <= 60:
        ducks["Darth Vader Ducky"] += 1
    elif 61 <= total_time <= 120:
        ducks["Thor Ducky"] += 1
    elif 121 <= total_time <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
    elif 181 <= total_time <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        number_of_tasks.append(task - 2)
        time_per_task.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{k}: {v}")for k, v in ducks.items()]
