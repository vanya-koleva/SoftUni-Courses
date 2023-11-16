first_match_result = input()
second_match_result = input()
third_match_result = input()
wins = 0
losses = 0
draws = 0

if ord(first_match_result[0]) > ord(first_match_result[2]):
    wins += 1
elif ord(first_match_result[0]) < ord(first_match_result[2]):
    losses += 1
else:
    draws += 1

if ord(second_match_result[0]) > ord(second_match_result[2]):
    wins += 1
elif ord(second_match_result[0]) < ord(second_match_result[2]):
    losses += 1
else:
    draws += 1

if ord(third_match_result[0]) > ord(third_match_result[2]):
    wins += 1
elif ord(third_match_result[0]) < ord(third_match_result[2]):
    losses += 1
else:
    draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")