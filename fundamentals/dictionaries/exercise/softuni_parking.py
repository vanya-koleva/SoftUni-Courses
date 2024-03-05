def display_parking(parking):
    for username, license_plate_number in parking.items():
        print(f"{username} => {license_plate_number}")


def process_unregister(parking, username):
    if username not in parking:
        print(f"ERROR: user {username} not found")
    else:
        del parking[username]
        print(f"{username} unregistered successfully")
    return parking


def process_register(parking, username, license_plate_number):
    if username in parking:
        print(f"ERROR: already registered with plate number {parking[username]}")
    else:
        parking[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")
    return parking


def main():
    parking = {}

    num = int(input())
    for _ in range(num):
        command = input().split()
        if "register" in command:
            command, username, license_plate_number = command
            parking = process_register(parking, username, license_plate_number)

        else:
            username = command[1]
            parking = process_unregister(parking, username)

    display_parking(parking)


main()
