def softuni_students(*args, **kwargs):
    students = {}
    courses = {}
    invalid_students = []
    result = ""

    for course_id, name in args:
        students[name] = course_id

    for course_id, course in kwargs.items():
        courses[course_id] = course

    for username, c_id in sorted(students.items()):
        if c_id in courses:
            course = courses[c_id]
            result += f"*** A student with the username {username} " \
                      f"has successfully finished the course {course}!\n"
        else:
            invalid_students.append(username)

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(invalid_students)}"

    return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
