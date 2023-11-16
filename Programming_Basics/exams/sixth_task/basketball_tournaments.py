name = input()
total_matches = 0
wins = 0
losses = 0

while name != "End of tournaments":
    number_of_matches = int(input())
    total_matches += number_of_matches
    counter_of_matches = 0
    for _ in range(number_of_matches):
        counter_of_matches += 1
        our_team_points = int(input())
        opposing_team_points = int(input())
        difference = abs(our_team_points - opposing_team_points)
        if our_team_points > opposing_team_points:
            wins += 1
            print(f"Game {counter_of_matches} of tournament {name}:"
                  f" win with {difference} points.")
        else:
            losses += 1
            print(f"Game {counter_of_matches} of tournament {name}: "
                  f"lost with {difference} points.")
    name = input()
else:
    wins_percentage = wins / total_matches * 100
    losses_percentage = losses / total_matches * 100
    print(f"{wins_percentage:.2f}% matches win")
    print(f"{losses_percentage:.2f}% matches lost")