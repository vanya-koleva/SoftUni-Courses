def process_take_skip(current_str_as_list, take_list, skip_list):
    hidden_message = ""
    while take_list and skip_list:
        taken_string = current_str_as_list[:take_list[0]]
        hidden_message += "".join(taken_string)
        current_str_as_list = current_str_as_list[take_list[0]:]
        current_str_as_list = current_str_as_list[skip_list[0]:]
        take_list.remove(take_list[0])
        skip_list.remove(skip_list[0])
    return hidden_message


def take_skip_rope(initial_str):
    numbers_list = [int(x) for x in initial_str if x.isdigit()]
    non_numbers_list = [x for x in initial_str if not x.isdigit()]
    take_list =[]
    skip_list = []
    for index, value in enumerate(numbers_list):
        if index % 2 == 0:
            take_list.append(value)
        else:
            skip_list.append(value)
    initial_str = process_take_skip(non_numbers_list, take_list, skip_list)
    return initial_str


initial_string = input()
print(take_skip_rope(initial_string))
