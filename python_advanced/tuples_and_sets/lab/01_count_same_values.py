nums = tuple([float(x) for x in input().split()])
occ = {}

for num in nums:
    if num not in occ:
        occ[num] = nums.count(num)

for num, count in occ.items():
    print(f"{num:.1f} - {count} times")
