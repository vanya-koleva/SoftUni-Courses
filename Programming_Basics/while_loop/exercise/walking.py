goal = 10000
total_steps = 0

while total_steps < goal:
    command = input()
    if command == 'Going home':
        current_steps = int(input())
        total_steps += current_steps
        break
    else:
        current_steps = int(command)
        total_steps += current_steps

difference = abs(total_steps - goal)
if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f'{difference} steps over the goal!')
else:
    print(f"{difference} more steps to reach goal.")