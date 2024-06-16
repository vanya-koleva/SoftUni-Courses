from collections import deque

monsters = deque(int(x) for x in input().split(","))
attacks = [int(x) for x in input().split(",")]
killed_monsters = 0

while monsters and attacks:
    monster = monsters.popleft()
    strike = attacks.pop()

    if strike >= monster:
        strike -= monster
        killed_monsters += 1
        if strike != 0:
            if attacks:
                attacks[-1] += strike
            else:
                attacks.append(strike)

    else:
        monster -= strike
        monsters.append(monster)

if not monsters:
    print("All monsters have been killed!")
if not attacks:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
