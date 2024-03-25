def process_sell(available_stock: dict, quantity_: int, food_name: str, number_of_sold_goods: int) -> int:
    if food_name not in available_stock.keys():
        print(f"You do not have any {food_name}.")

    elif available_stock[food_name] < quantity_:
        number_of_sold_goods += available_stock[food_name]
        print(f"There aren't enough {food_name}. You sold the last {available_stock[food_name]} of them.")
        del available_stock[food_name]

    else:
        available_stock[food_name] -= quantity_
        number_of_sold_goods  += quantity_
        print(f"You sold {quantity_} {food_name}.")
        if available_stock[food_name] == 0:
            del available_stock[food_name]

    return number_of_sold_goods


def process_receive(available_stock: dict, quantity_: int, food_name: str) -> None:
    if quantity_ <= 0:
        return
    elif food_name not in available_stock.keys():
        available_stock[food_name] = 0
    available_stock[food_name] += quantity_


def main():
    stock = {}
    sold_quantity = 0

    while True:
        command = input().split()
        if "Complete" in command:
            break

        command, quantity, food = command
        quantity = int(quantity)

        if command == "Receive":
            process_receive(stock, quantity, food)

        elif command == "Sell":
            sold_quantity = process_sell(stock, quantity, food, sold_quantity)

    for food, quantity in stock.items():
        print(f"{food}: {quantity}")
    print(f"All sold: {sold_quantity} goods")


if __name__ == '__main__':
    main()
