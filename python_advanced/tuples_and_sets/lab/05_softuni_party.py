reservations = set()

for _ in range(int(input())):
    reservations.add(input())

while True:
    res_num = input()

    if res_num == "END":
        break

    if res_num in reservations:
        reservations.remove(res_num)

print(len(reservations))

for i in sorted(reservations):
    print(i)
