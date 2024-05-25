nums = [string.split() for string in input().split("|")]
print(*[" ".join(x) for x in nums[::-1] if x])
