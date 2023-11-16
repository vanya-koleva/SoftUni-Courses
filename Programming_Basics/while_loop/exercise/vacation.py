needed_money = float(input())
available_money = float(input())
days_counter = 0
days_spending_counter = 0

while available_money < needed_money:
    command = input()
    amount = float(input())
    days_counter += 1
    if command == "spend":
        available_money -= amount
        if available_money < 0:
            available_money = 0
        days_spending_counter += 1
        if days_spending_counter >= 5:
            print("You can't save the money.")
            print(f"{days_counter}")
            break
    else:
        available_money += amount
        days_spending_counter = 0
else:
    print(f"You saved the money for {days_counter} days.")
