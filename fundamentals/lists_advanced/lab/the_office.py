employees = input().split()
improvement_factor = int(input())
happiness = list(map((lambda x: int(x) * improvement_factor), employees))
average_happiness = sum(happiness) / len(employees)
happy_employees = list(filter(lambda x: x >= average_happiness, happiness))

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")
