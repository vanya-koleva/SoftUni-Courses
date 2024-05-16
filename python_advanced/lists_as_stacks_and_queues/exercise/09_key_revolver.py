from collections import deque

price_bullets = int(input())
barrel_size = int(input())
bullets_stack = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
value_intelligence = int(input())
bullet_counter = 0

while locks and bullets_stack:
    lock = locks[0]

    bullet = bullets_stack.pop()
    bullet_counter += 1

    if bullet > lock:
        print("Ping!")
    else:
        print("Bang!")
        locks.popleft()

    if bullet_counter % barrel_size == 0 and bullets_stack:
        print("Reloading!")

if not locks:
    money_earned = value_intelligence - (price_bullets * bullet_counter)
    print(f"{len(bullets_stack)} bullets left. Earned ${money_earned}" )
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
    