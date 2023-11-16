number_of_bad_grades = int(input())
current_problem = input()
number_of_problems = 0
total_grades = 0
last_problem = ''
bad_grades_counter = 0

while current_problem != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == number_of_bad_grades:
            print(f"You need a break, {number_of_bad_grades} poor grades.")
            break
    number_of_problems += 1
    total_grades += current_grade
    last_problem = current_problem
    current_problem = input()
else:
    average_grades = total_grades / number_of_problems
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
