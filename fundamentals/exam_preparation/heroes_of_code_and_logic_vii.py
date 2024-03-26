def cast_spell(heroes, split_command):
    mp_needed = int(split_command[2])
    spell_name = split_command[3]

    if heroes[hero]["mp"] >= mp_needed:
        heroes[hero]["mp"] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mp']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")
    return heroes


def take_damage(heroes, split_command):
    damage = int(split_command[2])
    attacker = split_command[3]

    heroes[hero]["hp"] -= damage
    if heroes[hero]["hp"] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
    else:
        del heroes[hero]
        print(f"{hero} has been killed by {attacker}!")
    return heroes


def recharge(heroes, split_command):
    amount = int(split_command[2])
    if heroes[hero]["mp"] + amount > 200:
        amount_recovered = 200 - heroes[hero]["mp"]
        heroes[hero]["mp"] = 200
    else:
        heroes[hero]["mp"] += amount
        amount_recovered = amount
    print(f"{hero} recharged for {amount_recovered} MP!")
    return heroes


def heal(heroes, split_command):
    amount = int(split_command[2])
    if heroes[hero]["hp"] + amount > 100:
        amount_recovered = 100 - heroes[hero]["hp"]
        heroes[hero]["hp"] = 100
    else:
        heroes[hero]["hp"] += amount
        amount_recovered = amount
    print(f"{hero} healed for {amount_recovered} HP!")
    return heroes


number_of_heroes = int(input())
heroes_dict = {}
for hero in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    heroes_dict[hero_name] = {"hp": int(hp), "mp": int(mp)}

while True:
    command = input().split(" - ")
    if "End" in command:
        break
    hero = command[1]

    if "CastSpell" in command:
        heroes_dict = cast_spell(heroes_dict, command)
    elif "TakeDamage" in command:
        heroes_dict = take_damage(heroes_dict, command)
    elif "Recharge" in command:
        heroes_dict = recharge(heroes_dict, command)
    else:
        heroes_dict = heal(heroes_dict, command)

for hero, stats in heroes_dict.items():
    print(hero)
    print(f"HP: {stats['hp']}")
    print(f"MP: {stats['mp']}")
