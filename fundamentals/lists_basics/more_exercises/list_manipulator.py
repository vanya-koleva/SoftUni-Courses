# Convert the input string into a list of integers
numbers_list = list(map(int,input().split()))

while True:
    command_list = input().split()

    if "end" in command_list:
        print(numbers_list)
        break

    command = command_list[0]
    odds_list = [x for x in numbers_list if x % 2 != 0]
    evens_list = [x for x in numbers_list if x % 2 == 0]
    if command == "exchange":
        index = int(command_list[1])
        # Check if the index is valid
        if index > len(numbers_list) - 1 or index < 0:
            print("Invalid index")
            continue
        list1 = numbers_list[:index + 1]
        list2 = numbers_list[index + 1:]
        numbers_list = list2 + list1

    elif command == "max":
        if "even" in command_list:
            if evens_list:
                max_element = max(evens_list)
            else:
                print("No matches")
                continue
        else:
            if odds_list:
                max_element = max(odds_list)
            else:
                print("No matches")
                continue
        # Find the index of the maximum element from the end of the list
        right_max = numbers_list[::-1].index(max_element)
        # Calculate the index from the start of the list
        result = len(numbers_list) - 1 - right_max
        print(result)

    elif command == "min":
        if "even" in command_list:
            if evens_list:
                min_element = min(evens_list)
            else:
                print("No matches")
                continue
        else:
            if odds_list:
                min_element = min(odds_list)
            else:
                print("No matches")
                continue
        right_min = numbers_list[::-1].index(min_element)
        result = len(numbers_list) - 1 - right_min
        print(result)

    elif command == "first":
        count_of_elements = int(command_list[1])
        if count_of_elements > len(numbers_list):
            print("Invalid count")
        elif "even" in command_list:
            print(evens_list[:count_of_elements])
        else:
            print(odds_list[:count_of_elements])

    elif command == "last":
        count_of_elements = int(command_list[1])
        if count_of_elements > len(numbers_list):
            print("Invalid count")
        elif "even" in command_list:
            # Slice the last elements from the corresponding list
            last_even_numbers = (evens_list[-count_of_elements:])
            print(last_even_numbers)
        else:
            last_odd_numbers = (odds_list[-count_of_elements:])
            print(last_odd_numbers)
