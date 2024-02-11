def remove_and_insert_exercise(title_of_exercise, i):
    schedule.remove(title_of_exercise)
    schedule.insert(i + 1, title_of_exercise)


def swap_lessons(i1, i2):
    schedule[i1], schedule[i2] = schedule[i2], schedule[i1]


schedule = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    explode = command.split(":")
    lesson = explode[1]
    exercise = lesson + "-Exercise"
    if "Add" in explode:
        if lesson in schedule:
            continue
        schedule.append(lesson)

    elif "Insert" in explode:
        if lesson in schedule:
            continue
        schedule.insert(int(explode[2]), lesson)

    elif "Exercise" in explode:
        if lesson in schedule:
            index = schedule.index(lesson)
            if exercise not in schedule:
                schedule.insert(index + 1, exercise)
        else:
            schedule.append(lesson)
            schedule.append(exercise)

    elif "Remove" in explode:
        if lesson in schedule:
            schedule.remove(lesson)
            if exercise in schedule:
                schedule.remove(exercise)
    elif "Swap" in explode:
        lesson2 = explode[2]
        if lesson in schedule and lesson2 in schedule:
            exercise2 = lesson2 + "-Exercise"
            index1 = schedule.index(lesson)
            index2 = schedule.index(lesson2)
            if exercise in schedule and exercise2 in schedule:
                swap_lessons(index1, index2)
                remove_and_insert_exercise(exercise, index2)
                remove_and_insert_exercise(exercise2, index1)
            elif exercise in schedule:
                swap_lessons(index1, index2)
                remove_and_insert_exercise(exercise, index2)
            elif exercise2 in schedule:
                swap_lessons(index1, index2)
                remove_and_insert_exercise(exercise2, index1)
            else:
                swap_lessons(index1, index2)

for index, value in enumerate(schedule, 1):
    print(f"{index}.{value}")
