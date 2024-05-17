from collections import defaultdict

students = defaultdict(list)

for _ in range(int(input())):
    data = tuple(input().split())
    student, grade = data[0], float(data[1])
    students[student].append(grade)

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name} -> {' '.join(f'{x:.2f}' for x in grades)} (avg: {avg:.2f})")
