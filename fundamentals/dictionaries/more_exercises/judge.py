def display_results(users):
    print("Individual standings:")
    users_list = sorted(users.items(), key=lambda x: (-x[1], x[0]))
    for i, (username, total_points) in enumerate(users_list, start=1):
        print(f"{i}. {username} -> {total_points}")


def display_contests(contests, users):
    for contest_name, participants in contests.items():
        print(f"{contest_name}: {len(participants)} participants")

        participants_list = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
        for i, (username, points) in enumerate(participants_list, start=1):
            print(f"{i}. {username} <::> {points}")
            if username not in users:
                users[username] = 0
            users[username] += points


def register_submission(contests, username, contest, points):
    if contest not in contests:
        contests[contest] = {}
    if username not in contests[contest] or points > contests[contest][username]:
        contests[contest][username] = points
    return contests


def main():
    contests = {}
    users = {}

    while True:
        command = input().split(" -> ")

        if "no more time" in command:
            break

        username, contest, points = command
        points = int(points)

        contests = register_submission(contests, username, contest, points)

    display_contests(contests, users)
    display_results(users)


if __name__ == '__main__':
    main()
