def display_results(cities_dict) -> None:
    if cities_dict:
        print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
        for town, values in cities_dict.items():
            print(f"{town} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


def process_prosper(cities_dict, event: list) -> dict:
    town, gold = event[1], int(event[2])
    if gold > 0:
        cities_dict[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town]['gold']} gold.")
    else:
        print("Gold added cannot be a negative number!")
    return cities_dict


def process_plunder(cities_dict, event: list) -> dict:
    town, people, gold = event[1], int(event[2]), int(event[3])
    cities_dict[town]["population"] -= people
    cities_dict[town]["gold"] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    if cities_dict[town]["population"] == 0 or cities_dict[town]["gold"] == 0:
        del cities_dict[town]
        print(f"{town} has been wiped off the map!")
    return cities_dict


def get_events(cities_dict) -> dict:
    while True:
        event = input().split("=>")
        if "End" in event:
            break

        elif "Plunder" in event:
            cities_dict = process_plunder(cities_dict, event)
        elif "Prosper" in event:
            cities_dict = process_prosper(cities_dict, event)
    return cities_dict


def get_cities(cities_dict) -> dict:
    while True:
        command = input().split("||")
        if "Sail" in command:
            break

        town, population, gold = command

        if town not in cities:
            cities_dict[town] = {"population": 0, "gold": 0}
        cities_dict[town]["population"] += int(population)
        cities_dict[town]["gold"] += int(gold)
    return cities_dict


cities = {}
cities = get_cities(cities)
cities = get_events(cities)
display_results(cities)
