stops = input()
while True:
    command = input().split(":")
    if "Travel" in command:
        break

    elif "Add Stop" in command:
        index, some_string = int(command[1]), command[2]
        if index < len(stops):
            stops = stops[:index] + some_string + stops[index:]

    elif "Remove Stop" in command:
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif "Switch" in command:
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
