def display_cars(cars_dict) -> None:
    for car, values in cars_dict.items():
        print(f"{car} -> Mileage: {values['mileage']} kms, Fuel in the tank: {values['fuel']} lt.")


def revert(cars_dict, split_command: list) -> dict:
    car, kilometers = split_command[1], int(split_command[2])

    if cars_dict[car]["mileage"] - kilometers < 10000:
        cars_dict[car]["mileage"] = 10000
    else:
        cars_dict[car]["mileage"] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return cars_dict


def refuel(cars_dict, split_command: list) -> dict:
    car, fuel = split_command[1], int(split_command[2])

    if cars_dict[car]["fuel"] + fuel > 75:
        fuel = 75 - cars_dict[car]["fuel"]
        cars_dict[car]["fuel"] = 75
    else:
        cars_dict[car]["fuel"] += fuel

    print(f"{car} refueled with {fuel} liters")
    return cars_dict


def drive(cars_dict, split_command: list) -> dict:
    car, distance, needed_fuel = split_command[1], int(split_command[2]), int(split_command[3])

    if cars_dict[car]["fuel"] < needed_fuel:
        print("Not enough fuel to make that ride")
    else:
        cars_dict[car]["mileage"] += distance
        cars_dict[car]["fuel"] -= needed_fuel
        print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")

    if cars_dict[car]["mileage"] >= 100000:
        del cars_dict[car]
        print(f"Time to sell the {car}!")
    return cars_dict


def main():
    number_of_cars = int(input())
    cars = {}
    for _ in range(number_of_cars):
        command = input().split("|")
        car, mileage, fuel = command
        cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

    while True:
        command = input().split(" : ")
        if "Stop" in command:
            break

        elif "Drive" in command:
            cars = drive(cars, command)
        elif "Refuel" in command:
            cars = refuel(cars, command)
        elif "Revert" in command:
            cars = revert(cars, command)

    display_cars(cars)


if __name__ == '__main__':
    main()
