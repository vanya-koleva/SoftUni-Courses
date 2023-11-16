control_time_minutes = int(input())
control_time_seconds = int(input())
length = float(input())
seconds_per_100_meters = int(input())

control_time_in_seconds = control_time_minutes * 60 + control_time_seconds
deduction = length / 120
deducted_time = deduction * 2.5
time = (length / 100) * seconds_per_100_meters - deducted_time

if control_time_in_seconds < time:
    difference = abs(time - control_time_in_seconds)
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
else:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
