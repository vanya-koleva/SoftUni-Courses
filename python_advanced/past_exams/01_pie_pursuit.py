from collections import deque

contestants = deque(int(x) for x in input().split())
pies = [int(x) for x in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()

    if contestant >= pie:
        contestant -= pie
        if contestant > 0:
            contestants.append(contestant)

    else:
        pie -= contestant
        if pie == 1:
            if pies:
                pies[-1] += pie
            else:
                pies.append(pie)
        else:
            pies.append(pie)

if contestants and not pies:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in contestants)}")
elif pies and not contestants:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")
else:
    print("We have a champion!")
