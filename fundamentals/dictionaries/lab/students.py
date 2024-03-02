students = {}

while True:
    command = input().split(":")
    if len(command) == 1:
        break
    name, student_id, course = command
    if course not in students:
        students[course] = {}
    students[course][student_id] = name

course = command[0].replace("_", " ")
for key, value in students.items():
    if key == course:
        for student_id, name in value.items():
            print(f"{name} - {student_id}" )
