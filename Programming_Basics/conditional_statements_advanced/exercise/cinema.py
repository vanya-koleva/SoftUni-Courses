movie_type = input()
number_of_rows = int(input())
number_of_columns = int(input())
ticket_price = 0

if movie_type == 'Premiere':
    ticket_price = 12
elif movie_type == 'Normal':
    ticket_price = 7.5
elif movie_type == 'Discount':
    ticket_price = 5

seats = number_of_rows * number_of_columns
income = ticket_price * seats

print(f'{income:.2f} leva')
