import re

participants_list = input().split(", ")
participants = dict.fromkeys(participants_list, 0)

while True:
    info = input()
    if info == "end of race":
        break

    name = "".join(re.findall(r"[A-Za-z]+", info))
    digits = re.findall(r"\d", info)
    distance = sum(int(digit) for digit in digits)

    if name in participants:
        participants[name] += distance

sorted_participants = sorted(participants.items(), key=lambda x: -x[1])

print(f"1st place: {sorted_participants[0][0]}")
print(f"2nd place: {sorted_participants[1][0]}")
print(f"3rd place: {sorted_participants[2][0]}")
