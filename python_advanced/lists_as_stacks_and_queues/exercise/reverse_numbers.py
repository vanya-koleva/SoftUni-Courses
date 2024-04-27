from collections import deque

nums = deque(input().split())  #O(n)
for _ in range(len(nums)):
    print(nums.pop(), end=" ")

# numbers.reverse()
# print(*numbers)
