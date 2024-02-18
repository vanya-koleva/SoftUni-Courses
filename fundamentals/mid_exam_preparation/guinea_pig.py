food_in_gr = float(input()) * 1000
hay_in_gr = float(input()) * 1000
cover_in_gr = float(input()) * 1000
weight_in_gr = float(input()) * 1000
food_per_day = 300
cover_used_per_one_time = weight_in_gr / 3
everything_is_enough = True

for day in range(1, 31):
    if food_in_gr - food_per_day > 0:
        food_in_gr -= food_per_day
    else:
        everything_is_enough = False
        break

    if day % 2 == 0:
        hay_used = food_in_gr * 0.05
        if hay_in_gr - hay_used > 0:
            hay_in_gr -= hay_used
        else:
            everything_is_enough = False
            break

    if day % 3 == 0:
        if cover_in_gr - cover_used_per_one_time > 0:
            cover_in_gr -= cover_used_per_one_time
        else:
            everything_is_enough = False
            break


if everything_is_enough:
    food, hay, cover = food_in_gr / 1000, hay_in_gr / 1000, cover_in_gr / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
