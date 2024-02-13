def calculate_price(all_prices):
    total_price_without_taxes = sum(all_prices)
    taxes = sum(x * 0.20 for x in all_prices)
    return total_price_without_taxes, taxes


def calculate_total_price(price_without_taxes, additional_taxes, special):
    if special:
        total_price = price_without_taxes + additional_taxes
        total_price *= 0.90
        return total_price

    return price_without_taxes + additional_taxes


def computer_store():
    prices = []
    is_special_client = False

    while True:
        command = input()

        if command == "special" or command == "regular":
            if not prices:
                return "Invalid order!"

            if command == "special":
                is_special_client = True
                break

            elif command == "regular":
                break

        price = float(command)
        if price <= 0:
            print("Invalid price!")
            continue

        prices.append(price)

    total_price_without_taxes, taxes = calculate_price(prices)
    total_price_with_taxes = calculate_total_price(total_price_without_taxes, taxes, is_special_client)

    return process_receipt(total_price_with_taxes, total_price_without_taxes, taxes)


def process_receipt(price_with_taxes, price_without_taxes, the_taxes):
    return f"Congratulations you've just bought a new computer!\n" \
           f"Price without taxes: {price_without_taxes:.2f}$\n" \
           f"Taxes: {the_taxes:.2f}$\n" \
           f"-----------\n" \
           f"Total price: {price_with_taxes:.2f}$"


print(computer_store())
