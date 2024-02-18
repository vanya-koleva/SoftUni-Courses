def bonus_scoring_system(number_of_students, total_number_of_lectures, additional_bonus):
    max_bonus_points = 0
    max_student_attendances = 0

    for current_student in range(number_of_students):
        attendances = int(input())
        total_bonus = attendances / total_number_of_lectures * (5 + additional_bonus)
        if total_bonus > max_bonus_points:
            max_bonus_points = total_bonus
            max_student_attendances = attendances

    return max_bonus_points, max_student_attendances


def print_result(max_bonus_points, max_student_attendances):
    print(f"Max Bonus: {round(max_bonus_points)}.")
    print(f"The student has attended {max_student_attendances} lectures.")


number_of_students_ = int(input())
total_number_of_lectures_ = int(input())
additional_bonus_ = int(input())
bonus_points, student_attendances = bonus_scoring_system(number_of_students_, total_number_of_lectures_, additional_bonus_)
print_result(bonus_points, student_attendances)
