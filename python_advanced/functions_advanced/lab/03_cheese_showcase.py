def sorting_cheeses(**kwargs):
    result = ""
    cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for name, quantities in cheeses:
        result += f"{name}\n"

        for quantity in sorted(quantities, reverse=True):
            result += f"{quantity}\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
