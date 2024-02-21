def the_lift(people, lift):
    max_size_of_wagon = 4
    for i in range(len(lift)):
        free_spaces = max_size_of_wagon - lift[i]

        if people >= free_spaces:
            lift[i] += free_spaces
        else:
            lift[i] += people

        people -= free_spaces

        if people <= 0 and (i != len(lift) - 1 or lift[i] < max_size_of_wagon):
            print("The lift has empty spots!")
            break

    else:
        if people > 0:
            print(f"There isn't enough space! {people} people in a queue!")

    lift = [str(x) for x in lift]
    return " ".join(lift)


number_of_people = int(input())
lift_ = [int(x) for x in input().split()]
print(the_lift(number_of_people, lift_))
