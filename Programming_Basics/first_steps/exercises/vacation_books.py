number_of_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_book = number_of_pages / pages_per_hour
hours_per_day = hours_per_book / days
print(int(hours_per_day))