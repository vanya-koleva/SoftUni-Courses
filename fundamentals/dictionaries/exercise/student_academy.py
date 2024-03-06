def display_students(students):
    for name, grades in students.items():
        average_grade = sum(grades) / len(grades)
        if average_grade >= 4.5:
            print(f"{name} -> {average_grade:.2f}")


def main():
    students = {}
    number_of_grades = int(input())

    for i in range(number_of_grades):
        student_name = input()
        grade = float(input())

        if student_name not in students:
            students[student_name] = []

        students[student_name].append(grade)

    display_students(students)


if __name__ == '__main__':
    main()
