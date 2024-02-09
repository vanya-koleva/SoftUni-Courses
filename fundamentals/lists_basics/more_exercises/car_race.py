sequence_of_numbers = input().split()
middle_index = len(sequence_of_numbers) // 2
left_side = sequence_of_numbers[:middle_index]
right_side = sequence_of_numbers[middle_index + 1:]
left_side_time = 0
right_side_time = 0

for time in left_side:
    if int(time) == 0:
        left_side_time *= 0.8
    else:
        left_side_time += int(time)

for time in right_side[:: - 1]:
    if int(time) == 0:
        right_side_time *= 0.8
    else:
        right_side_time += int(time)

if left_side_time < right_side_time:
    print(f"The winner is left with total time: {left_side_time:.1f}")
else:
    print(f"The winner is right with total time: {right_side_time:.1f}")
