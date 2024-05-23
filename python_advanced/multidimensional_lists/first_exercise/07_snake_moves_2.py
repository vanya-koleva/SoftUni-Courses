from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())

snake = deque(word)
step = 1

for i in range(rows):
    while len(snake) < cols:
        snake.extend(word)

    print(*[snake.popleft() for _ in range(cols)][::step], sep="")
    step *= -1
