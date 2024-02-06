def loading_bar(some_number: int):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    percent_symbols = some_number // 10
    return f"{some_number}% [{'%' * percent_symbols}{'.' * (10 - percent_symbols)}]\nStill loading..."


percents = int(input())
print(loading_bar(percents))
