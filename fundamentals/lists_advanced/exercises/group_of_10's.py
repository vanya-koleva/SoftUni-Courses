numbers = [int(x) for x in input().split(", ")]
group = 10

while numbers:
    filtered_numbers = [x for x in numbers if x <= group]
    print(f"Group of {group}'s: {filtered_numbers}")
    numbers = [x for x in numbers if x not in filtered_numbers]
    group += 10
