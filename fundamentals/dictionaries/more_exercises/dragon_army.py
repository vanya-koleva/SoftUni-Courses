from collections import defaultdict


def display_dragons(dragons: dict) -> None:
    for dragon_type, stats in dragons.items():
        damage_stats = [x[0] for x in stats.values()]
        damage = sum(damage_stats) / len(damage_stats)
        health = sum(x[1] for x in stats.values()) / len(stats)
        armor = sum(x[2] for x in stats.values()) / len(stats)
        print(f"{dragon_type}::({damage:.2f}/{health:.2f}/{armor:.2f})")
        for name, stat in sorted(stats.items()):
            print(f"-{name} -> damage: {stat[0]}, health: {stat[1]}, armor: {stat[2]}")


def process_input(dragons: dict, defaults: dict, n: int) -> dict:
    for _ in range(n):
        dragon_type, name, damage, health, armor = input().split()

        if health == "null":
            health = defaults["health"]
        if damage == "null":
            damage = defaults["damage"]
        if armor == "null":
            armor = defaults["armor"]

        dragons[dragon_type][name] = [int(damage), int(health), int(armor)]
    return dragons


num = int(input())
dragons_dict = defaultdict(dict)
default_values = {"health": 250, "damage": 45, "armor": 10}
dragons_dict = process_input(dragons_dict, default_values, num)
display_dragons(dragons_dict)
