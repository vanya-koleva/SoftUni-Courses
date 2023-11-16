actor_name = input()
total_points = float(input())
count_of_graders = int(input())

for i in range(count_of_graders):
    name_of_grader = input()
    points_from_grader = float(input())
    received_points = len(name_of_grader) * points_from_grader / 2
    total_points += received_points
    if total_points >= 1250.5:
        break
difference = abs(1250.5 - total_points)
if total_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")