name = input()
total_grades = 0
fails = 0
current_class = 1

while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails > 1:
            print(f"{name} has been excluded at {current_class} grade")
            break
        continue
    current_class += 1
    total_grades += grade
    if current_class > 12:
        average = total_grades / 12
        print(f"{name} graduated. Average grade: {average:.2f}")
        break