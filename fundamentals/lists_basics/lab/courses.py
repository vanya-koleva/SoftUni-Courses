number_of_courses = int(input())
courses = []

for current_course in range(number_of_courses):
    course_name = input()
    courses.append(course_name)

print(courses)
