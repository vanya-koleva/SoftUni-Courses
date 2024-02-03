events = input().split("|")
energy = 100
coins = 100

for event in events:
    event_name, event_value = event.split("-")
    event_value = int(event_value)
    if event_name == "rest":
        if energy + event_value > 100:
            event_value = 100 - energy
            energy = 100
        else:
            energy += event_value
        print(f"You gained {event_value} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":
        if energy >= 30:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            break

else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
