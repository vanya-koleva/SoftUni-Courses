def process_merge(a_list, start_index, end_index):
    start_index = max(0, start_index)
    end_index = min(len(a_list) - 1, end_index)
    a_list[start_index:end_index + 1] = [''.join(a_list[start_index:end_index + 1])]


def process_divide(b_list, index, partitions):
    element = b_list[index]
    new_elements = []
    average_partition_length = len(element) // partitions
    last_partition_length = len(element) - average_partition_length * (partitions - 1)
    for i in range(partitions - 1):
        new_elements.append(element[i * average_partition_length:(i + 1) * average_partition_length])
    new_elements.append(element[-last_partition_length:])
    b_list.remove(b_list[index])
    for i, new_element in enumerate(new_elements):
        b_list.insert(index + i, new_element)


def process_strings(some_list):
    while True:
        command = input()
        if command == "3:1":
            return " ".join(some_list)
        command = command.split()
        if "merge" in command:
            process_merge(some_list, int(command[1]), int(command[2]))
        elif "divide" in command:
            process_divide(some_list, int(command[1]), int(command[2]))


list_of_strings = input().split()
print(process_strings(list_of_strings))
