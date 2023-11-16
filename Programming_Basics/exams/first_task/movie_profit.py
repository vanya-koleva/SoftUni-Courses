movie_name = input()
days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
percent_for_the_cinema = int(input())

profit_per_day = ticket_price * number_of_tickets
total_sum = days * profit_per_day
percent_for_the_cinema = percent_for_the_cinema / 100 * total_sum
total_sum -= percent_for_the_cinema


print(f"The profit from the movie {movie_name} is {total_sum:.2f} lv.")