import re

demons = input().replace(' ', '').split(',')
sorted_demons = sorted(demons)
pattern_nums = r"[-+]?\d+(?:\.\d+)?"

for demon in sorted_demons:
    health = sum([ord(ch) for ch in demon if not ch.isdigit() and ch not in ['+', '-', '*', '/', '.']])
    nums = re.findall(pattern_nums, demon)
    damage = 0
    if nums:
        damage = sum([float(x) for x in nums])
    special_actions = []

    for i in range(len(demon)):
        if demon[i] == "*" or demon[i] == "/":
            special_actions.append(demon[i])

    if special_actions:
        for action in special_actions:
            if action == "*":
                damage *= 2
            elif action == "/":
                damage /= 2

    print(f"{demon} - {health} health, {damage:.2f} damage")
