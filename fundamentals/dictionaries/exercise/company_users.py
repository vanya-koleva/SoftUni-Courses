def display_companies(company_users):
    for company_name, employees in company_users.items():
        print(company_name)
        for employee_id in employees:
            print(f"-- {employee_id}")


def main():
    company_users = {}

    while True:
        command = input().split(" -> ")

        if "End" in command:
            break

        company_name, employee_id = command

        if company_name not in company_users:
            company_users[company_name] = []

        if employee_id not in company_users[company_name]:
            company_users[company_name].append(employee_id)

    display_companies(company_users)


if __name__ == '__main__':
    main()
