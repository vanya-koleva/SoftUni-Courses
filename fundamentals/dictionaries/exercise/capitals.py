countries = input().split(", ")
capitals = input().split(", ")
dictionary = dict(zip(countries, capitals))

for country, capital in dictionary.items():
    print(f"{country} -> {capital}")
