first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
number_of_students = int(input())
hours = 0
max_capacity_per_hour = first_employee_capacity + second_employee_capacity + third_employee_capacity

while number_of_students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    number_of_students -= max_capacity_per_hour

print(f"Time needed: {hours}h.")
