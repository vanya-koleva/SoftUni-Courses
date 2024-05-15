from collections import deque

data = deque(input())
opening = "({["
closing = ")}]"
counter = 0

while data and counter < len(data) / 2:
    if data[0] in closing:
        break

    index = opening.index(data[0])
    if data[1] == closing[index]:
        data.popleft()
        data.popleft()
        data.rotate(counter)
        counter = 0
    else:
        data.rotate(-1)
        counter += 1

if data:
    print("NO")
else:
    print("YES")
