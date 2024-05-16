from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
counter = 0
crash = False

command = input()
while command != "END":

    if command != "green":
        cars.append(command)
    else:
        current_green = green_light

        while cars and current_green > 0:
            car = cars.popleft()
            time = current_green + free_window

            if len(car) > time:
                print("A crash happened!")
                print(f"{car} was hit at {car[time]}.")
                crash = True
                break

            current_green -= len(car)
            counter += 1

    if crash:
        break

    command = input()

else:
    print("Everyone is safe.")
    print(f"{counter} total cars passed the crossroads.")
