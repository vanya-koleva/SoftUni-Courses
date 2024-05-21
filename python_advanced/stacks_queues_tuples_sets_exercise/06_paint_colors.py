from collections import deque

substrings = deque(input().split())

colors = ["red", "yellow", "blue", "orange", "purple", "green"]

sec_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

result = []

while substrings:
    first_string = substrings.popleft()
    second_string = substrings.pop() if substrings else ""

    for word in (first_string + second_string, second_string + first_string):
        if word in colors:
            result.append(word)
            break

    else:
        for el in (first_string[:-1], second_string[:-1]):
            if el:
                substrings.insert(len(substrings) // 2, el)

for color in set(sec_colors.keys()).intersection(result):
    if not sec_colors[color].issubset(result):
        result.remove(color)

print(result)
