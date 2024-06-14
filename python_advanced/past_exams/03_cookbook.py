def cookbook(*args):
    recipes = {}
    result = ""

    for recipe in args:
        name, cuisine, ingredients = recipe
        recipes.setdefault(cuisine, {})[name] = ingredients

    sorted_recipes = dict(sorted(recipes.items(), key=lambda x: (-len(x[1]), x[0])))
    for cuisine, elements in sorted_recipes.items():
        result += f"{cuisine} cuisine contains {len(elements)} recipes:\n"
        for name, ingredients in sorted(elements.items()):
            result += f"  * {name} -> Ingredients: {', '.join(ingredients)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
