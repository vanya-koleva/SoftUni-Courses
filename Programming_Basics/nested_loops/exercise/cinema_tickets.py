movie_name = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie_name != "Finish":
    capacity = int(input())
    sold_seats = 0
    for _ in range(capacity):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        sold_seats += 1
    full_percentage = sold_seats / capacity * 100
    print(f"{movie_name} - {full_percentage:.2f}% full.")
    movie_name = input()
else:
    total_tickets = student_tickets + standard_tickets + kid_tickets
    student_tickets_percentage = student_tickets / total_tickets * 100
    standard_tickets_percentage = standard_tickets / total_tickets * 100
    kid_tickets_percentage = kid_tickets / total_tickets * 100
    print(f"Total tickets: {total_tickets}")
    print(f"{student_tickets_percentage:.2f}% student tickets.")
    print(f"{standard_tickets_percentage:.2f}% standard tickets.")
    print(f"{kid_tickets_percentage:.2f}% kids tickets.")