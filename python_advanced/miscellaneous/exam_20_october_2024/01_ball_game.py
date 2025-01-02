from collections import deque

strengths = [int(x) for x in input().split()]
accuracies = deque(int(x) for x in input().split())
scored_goals = 0

while strengths and accuracies:
    strength, accuracy = strengths.pop(), accuracies.popleft()
    resulting_sum = strength + accuracy

    if resulting_sum == 100:
        scored_goals += 1
    elif resulting_sum < 100:
        if strength < accuracy:
            accuracies.appendleft(accuracy)
        elif strength > accuracy:
            strengths.append(strength)
        else:
            strengths.append(resulting_sum)
    else:
        strengths.append(strength - 10)
        accuracies.append(accuracy)

if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals == 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")

if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")

if strengths:
    print(f"Strength values left: {', '.join(map(str, strengths))}")

if accuracies:
    print(f"Accuracy values left: {', '.join(map(str, accuracies))}")
