def check_column(num):
    for index in range(2):
        if first_line[index] == num and second_line[index] == num and third_line[index] == num:
            return True


def check_diagonal(num):
    if first_line[0] == num and second_line[1] == num and third_line[2] == num:
        return True
    elif first_line[2] == num and second_line[1] == num and third_line[0] == num:
        return True


def determine_winner(num):
    if first_line.count(num) == 3 or second_line.count(num) == 3 or third_line.count(num) == 3:
        return True
    elif check_column(num):
        return True
    elif check_diagonal(num):
        return True


first_line = list(map(int,(input().split())))
second_line = list(map(int,(input().split())))
third_line = list(map(int,(input().split())))

if determine_winner(1):
    print("First player won")
elif determine_winner(2):
    print("Second player won")
else:
    print("Draw!")
