clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_needed = 0

while clothes:
    racks_needed += 1
    current_capacity = rack_capacity
    while clothes and current_capacity - clothes[-1] >= 0:
        current_capacity -= clothes.pop()

print(racks_needed)
