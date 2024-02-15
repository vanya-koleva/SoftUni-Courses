energy = int(input())
command = input()
have_energy = True
battles = 0

while command != "End of battle":
    distance = int(command)
    if energy - distance < 0:
        have_energy = False
        break

    energy -= distance
    battles += 1
    if battles % 3 == 0:
        energy += battles

    command = input()

if have_energy:
    print(f"Won battles: {battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {battles} won battles and {energy} energy")
