def display_courses(courses):
    for course, students in courses.items():
        print(f"{course}: {len(students)}")
        for student_name in students:
            print(f"-- {student_name}")


def main():
    courses = {}

    while True:
        command = input().split(" : ")

        if "end" in command:
            break

        course_name, student_name = command

        if course_name not in courses.keys():
            courses[course_name] = []

        courses[course_name].append(student_name)

    display_courses(courses)


if __name__ == '__main__':
    main()
