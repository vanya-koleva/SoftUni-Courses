from collections import deque


def hot_potato(names: deque, toss: int) -> str:
    while len(names) > 1:
        names.rotate(-toss)
        print(f"Removed {names.popleft()}")
    return names[0]


kids = deque(input().split())
toss_num = int(input()) - 1
last_kid = hot_potato(kids, toss_num)
print(f"Last is {last_kid}")
