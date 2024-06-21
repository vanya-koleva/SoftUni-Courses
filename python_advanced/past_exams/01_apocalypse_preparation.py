from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament= medicaments.pop()

    combination = textile + medicament
    if combination == 30:
        created_items["Patch"] += 1
    elif combination == 40:
        created_items["Bandage"] += 1
    elif combination >= 100:
        created_items["MedKit"] += 1
        if medicaments:
            next_med = medicaments.pop()
            medicaments.append(next_med + (combination - 100))
    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item, amount in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
    if amount:
        print(f"{item} - {amount}")

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}")
elif textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
