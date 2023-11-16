number_of_tournaments = int(input())
starting_points = int(input())
total_points = 0
tournaments_won = 0

for i in range(number_of_tournaments):
    position = input()
    if position == 'W':
        total_points += 2000
        tournaments_won += 1
    elif position == 'F':
        total_points += 1200
    else:
        total_points += 720

tournaments_won_percentage = tournaments_won / number_of_tournaments * 100
average_points = int(total_points / number_of_tournaments)
total_points += starting_points

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{tournaments_won_percentage:.02f}%")