from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while substances and tools:
    if not challenges:
        break
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
        continue

    tools.append(tool + 1)
    if substance - 1 > 0:
        substances.append(substance - 1)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
