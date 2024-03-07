def print_results(results):
    print("Results:")
    for username, language in results.items():
        max_result = max(language.values())
        print(f"{username} | {max_result}")


def print_number_of_submissions(number_of_submissions):
    print("Submissions:")
    for language, count in number_of_submissions.items():
        print(f"{language} - {count}")


def process_submission(results, username, language, points, number_of_submissions):
    if language not in number_of_submissions:
        number_of_submissions[language] = 0
    number_of_submissions[language] += 1

    if username in results:
        if language in results[username]:
            results[username][language] = max(results[username][language], points)
        else:
            results[username][language] = points
    else:
        results[username] = {language: points}


def main():
    results = {}
    number_of_submissions = {}
    bans = []

    while True:
        command = input().split("-")

        if "exam finished" in command:
            break

        elif "banned" in command:
            username = command[0]
            bans.append(username)

        else:
            username, language, points = command
            points = int(points)
            process_submission(results, username, language, points, number_of_submissions)

    for user in bans:
        if user in results:
            del results[user]

    print_results(results)
    print_number_of_submissions(number_of_submissions)


if __name__ == '__main__':
    main()
