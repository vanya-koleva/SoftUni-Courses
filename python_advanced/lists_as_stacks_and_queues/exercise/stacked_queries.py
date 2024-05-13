def display_stack(stack):
    stack.reverse()
    print(*stack, sep=", ")


def process_commands(stack, query):
    commands = {
        "1": lambda x: stack.append(int(x[1])),
        "2": lambda x: stack.pop() if stack else None,
        "3": lambda x: print(max(stack)) if stack else None,
        "4": lambda x: print(min(stack)) if stack else None
    }
    command = query[0]
    commands[command](query)


def solution():
    stack = []
    for _ in range(int(input())):
        query = input().split()
        process_commands(stack, query)

    display_stack(stack)


solution()
