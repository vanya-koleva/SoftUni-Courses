number_of_movies = int(input())
max_rating = 0
max_rating_name = ""
min_rating_name = ""
min_rating = 11
all_ratings = 0

for _ in range(number_of_movies):
    movie_name = input()
    rating = float(input())
    all_ratings += rating
    if max_rating < rating:
        max_rating = rating
        max_rating_name = movie_name
    if min_rating > rating:
        min_rating = rating
        min_rating_name = movie_name

average_rating = all_ratings / number_of_movies
print(f"{max_rating_name} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_name} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")