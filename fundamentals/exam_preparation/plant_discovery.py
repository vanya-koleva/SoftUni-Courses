def display_plants(plants: dict) -> None:
    print("Plants for the exhibition:")
    for plant, info in plants.items():
        if "rating" in info:
            average_rating = sum(info["rating"]) / len(info["rating"])
        else:
            average_rating = 0
        print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")


def reset(plants: dict, plant: str) -> dict:
    del plants[plant]["rating"]
    return plants


def update(plants: dict, plant: str, new_rarity: str) -> dict:
    plants[plant]["rarity"] = int(new_rarity)
    return plants


def rate(plants: dict, plant: str, rating: str) -> dict:
    plants[plant].setdefault("rating", [])
    plants[plant]["rating"].append(int(rating))
    return plants


def check_plant(plants: dict, plant: str) -> bool:
    if plant not in plants:
        print("error")
        return False
    else:
        return True


def main():
    plants = {}
    num = int(input())
    for _ in range(num):
        info = input().split("<->")
        plant, rarity = info
        plants[plant] = {"rarity": int(rarity)}

    while True:
        command = input().split(": ")
        if "Exhibition" in command:
            break

        action, info = command
        if action == "Rate":
            plant, rating = info.split(" - ")
            if check_plant(plants, plant):
                plants = rate(plants, plant, rating)

        elif action == "Update":
            plant, new_rarity = info.split(" - ")
            if check_plant(plants, plant):
                plants = update(plants, plant, new_rarity)

        else:
            plant = info
            if check_plant(plants, plant):
                plants = reset(plants, plant)

    display_plants(plants)


if __name__ == '__main__':
    main()
