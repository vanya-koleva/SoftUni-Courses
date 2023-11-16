best_player = ""
most_goals = 0
hat_trick = False
name = input()
while name != "END":
    goals = int(input())
    if goals > most_goals:
        most_goals = goals
        best_player = name
    if goals >= 3:
        hat_trick = True
    if goals >= 10:
        break
    name = input()

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")