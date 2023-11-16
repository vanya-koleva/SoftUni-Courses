vacation_days = int(input())
working_days = 365 - vacation_days
playtime = vacation_days * 127 + working_days * 63
difference = abs(30000 - playtime)
hours = difference // 60
minutes = difference % 60

if playtime <= 30000:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")