def display_results(submissions):
    user = ""
    total_points = 0

    for participant, contests in submissions.items():
        points = sum(contests.values())
        if points > total_points:
            total_points = points
            user = participant
    print(f"Best candidate is {user} with total {total_points} points.")

    print("Ranking:")
    submissions = dict(sorted(submissions.items()))
    for user_name, contests in submissions.items():
        print(f"{user_name}")
        contests = dict(sorted(contests.items(), key=lambda x: x[1], reverse=True))
        for contest, points in contests.items():
            print(f"#  {contest} -> {points}")


def add_user(submissions, contest, username, points):
    if username not in submissions.keys():
        submissions[username] = {contest: points}
    else:
        if contest not in submissions[username]:
            submissions[username].update({contest: points})
        else:
            submissions[username][contest] = max(submissions[username][contest], points)


def check_validity(contests, contest, password):
    for key, value in contests.items():
        if key == contest and value == password:
            return True
    return False


def main():
    contests = {}
    submissions = {}

    while True:
        command = input().split(":")

        if "end of contests" in command:
            break

        contest, password = command
        contests[contest] = password

    while True:
        command = input().split("=>")

        if "end of submissions" in command:
            break

        contest, password, username, points = command
        points = int(points)

        is_valid = check_validity(contests, contest, password)
        if is_valid:
            add_user(submissions, contest, username, points)

    display_results(submissions)


if __name__ == '__main__':
    main()
