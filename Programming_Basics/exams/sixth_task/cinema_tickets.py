student_tickets_counter = 0
standard_tickets_counter = 0
kid_tickets_counter = 0

while True:
    movie_name = input()
    total_tickets = 0
    if movie_name == "Finish":
        break
    capacity = int(input())
    for _ in range(capacity):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter += 1
        elif ticket_type == "standard":
            standard_tickets_counter += 1
        elif ticket_type == "kid":
            kid_tickets_counter += 1
        total_tickets += 1
    percentage_full = total_tickets / capacity * 100
    print(f"{movie_name} - {percentage_full:.2f}% full.")

all_tickets = standard_tickets_counter + student_tickets_counter + kid_tickets_counter
student_tickets_percentage = student_tickets_counter / all_tickets * 100
standard_tickets_percentage = standard_tickets_counter / all_tickets * 100
kid_tickets_percentage = kid_tickets_counter / all_tickets * 100
print(f"Total tickets: {all_tickets}")
print(f"{student_tickets_percentage:.2f}% student tickets.")
print(f"{standard_tickets_percentage:.2f}% standard tickets.")
print(f"{kid_tickets_percentage:.2f}% kids tickets.")