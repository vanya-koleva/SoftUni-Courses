def solution(some_list, k):
    executed_people = []
    # Calculate the initial index from where execution starts
    index = (k - 1) % len(some_list)

    while some_list:
        # Pop the person at the current index from the list and append to the executed_people list
        executed_people.append(some_list.pop(index))
        if some_list:
            # current index + the step in order to continue the circle
            index = (index + k - 1) % len(some_list)
    return ",".join(executed_people)


list_of_people = input().split()
person_to_be_executed = int(input())
print(f"[{solution(list_of_people, person_to_be_executed)}]")
