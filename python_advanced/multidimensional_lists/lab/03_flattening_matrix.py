rows = int(input())
flattened = []

for _ in range(rows):
    data = [int(x) for x in input().split(", ")]
    flattened.extend(data)

print(flattened)
