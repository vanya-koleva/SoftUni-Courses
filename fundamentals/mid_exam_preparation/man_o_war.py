def man_o_war(pirate_ship, warship, maximum_health):
    while True:
        command = input()
        if command == "Retire":
            return f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}"

        elif command == "Status":
            minimum_health = maximum_health * 0.2
            sections_to_repair = [x for x in pirate_ship if x < minimum_health]
            print(f"{len(sections_to_repair)} sections need repair.")

        explode = command.split()

        if "Fire" in explode:
            index = int(explode[1])
            damage = int(explode[2])

            if 0 <= index <= len(warship) -1:
                warship[index] -= damage

                if warship[index] <= 0:
                    return "You won! The enemy ship has sunken."

        elif "Defend" in explode:
            start_index = int(explode[1])
            end_index = int(explode[2])
            damage = int(explode[3])

            if 0 <= start_index <= len(pirate_ship) -1 and 0 <= end_index <= len(pirate_ship) -1:
                for i in range(start_index, end_index +1):
                    pirate_ship[i] -= damage
                    if pirate_ship[i] <= 0:
                        return "You lost! The pirate ship has sunken."

        elif "Repair" in explode:
            index = int(explode[1])
            health = int(explode[2])

            if 0 <= index <= len(pirate_ship) -1:
                pirate_ship[index] += health
                if pirate_ship[index] > maximum_health:
                    pirate_ship[index] = maximum_health


pirate_ship_ = [int(x) for x in input().split(">")]
warship_ = [int(x) for x in input().split(">")]
maximum_health_capacity = int(input())
print(man_o_war(pirate_ship_, warship_, maximum_health_capacity))
