def process_command(command, number, health, bitcoins, is_dead):
    if command == "potion":
        if health + number > 100:
            amount_healed = 100 - health
            health = 100
        else:
            health += number
            amount_healed = number

        print(f"You healed for {amount_healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        amount_of_bitcoins = number
        bitcoins += number
        print(f"You found {amount_of_bitcoins} bitcoins.")

    else:
        health -= number
        if health <= 0:
            is_dead = True
        else:
            print(f"You slayed {command}.")

    return health, bitcoins, is_dead


def mu_online(list_of_rooms):
    health = 100
    bitcoins = 0
    is_dead = False
    for room in range(1, len(list_of_rooms) + 1):
        explode = list_of_rooms[room - 1].split()
        command = explode[0]
        number = int(explode[1])
        health, bitcoins, is_dead = process_command(command, number, health, bitcoins, is_dead)
        if is_dead:
            print(f"You died! Killed by {command}." )
            print(f"Best room: {room}")
            break

    else:
        print(f"You've made it!")
        print(f"Bitcoins: {bitcoins}")
        print(f"Health: {health}")


dungeon_rooms = input().split("|")
mu_online(dungeon_rooms)
