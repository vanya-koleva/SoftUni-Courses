from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk = deque(int(x) for x in input().split(", "))
milkshakes = 0

while milkshakes < 5 and milk and chocolates:
    curr_choco = chocolates.pop()
    curr_milk = milk.popleft()

    if curr_choco <= 0 and curr_milk <= 0:
        continue
    elif curr_choco <= 0:
        milk.appendleft(curr_milk)
        continue
    elif curr_milk <= 0:
        chocolates.append(curr_choco)
        continue

    if curr_choco == curr_milk:
        milkshakes += 1
    else:
        milk.append(curr_milk)
        chocolates.append(curr_choco - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk) or 'empty'}")
