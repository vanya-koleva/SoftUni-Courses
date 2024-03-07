def display_forces(forces):
    for force_side, users in forces.items():
        if len(users) != 0:
            print(f"Side: {force_side}, Members: {len(users)}")
            for force_user in users:
                print(f"! {force_user}")


def check_user(forces, force_user):
    user_found = False
    for force, users in forces.items():
        if force_user in users:
            user_found = True
    return user_found


def remove_user(forces, force_user):
    for force, users in forces.items():
        if force_user in users:
            users.remove(force_user)
            break


def create_side_or_user(forces, force_side, force_user):
    if force_user not in forces.values():
        if force_side not in forces.keys():
            forces[force_side] = []
        forces[force_side].append(force_user)


def main():
    forces = {}

    while True:
        command = input().split(" | ")

        if "Lumpawaroo" in command:
            break

        if len(command) == 2:  #if split was successful
            force_side, force_user = command
            user_found = check_user(forces, force_user)
            if not user_found:
                create_side_or_user(forces, force_side, force_user)

        else:
            command = "".join(command).split(" -> ")
            force_user, force_side = command
            user_found = check_user(forces, force_user)

            if user_found:
                remove_user(forces, force_user)
            create_side_or_user(forces, force_side, force_user)

            print(f"{force_user} joins the {force_side} side!")

    display_forces(forces)


if __name__ == '__main__':
    main()
