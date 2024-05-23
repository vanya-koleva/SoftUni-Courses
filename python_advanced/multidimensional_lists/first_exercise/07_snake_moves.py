from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(list(input()))

for i in range(rows):
    line = []
    for _ in range(cols):
        char = snake.popleft()
        line.append(char)
        snake.append(char)

    if i % 2 == 0:
        print(*line, sep="")
    else:
        print(*line[::-1], sep="")
