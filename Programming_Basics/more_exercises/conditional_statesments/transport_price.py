distance = int(input())
time = input()
total = 0

if distance < 20:
    if time == 'day':
        total = distance * 0.79 + 0.70
    else:
        total = distance * 0.90 + 0.70
elif 20 <= distance < 100:
    total = distance * 0.09
else:
    total = distance * 0.06

print(f"{total:.02f}")