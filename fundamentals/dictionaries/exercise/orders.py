def print_total_price(products):
    for product_name, value in products.items():
        total_price = value["quantity"] * value["price"]
        print(f"{product_name} -> {total_price:.2f}")


def get_products(products):
    while True:
        command = input().split()
        if "buy" in command:
            break

        product, price, quantity = command
        price = float(price)
        quantity = int(quantity)

        if product not in products.keys():
            products[product] = {"quantity":0}
        products[product]["quantity"] += quantity

        products[product]["price"] = price

    return products


products_ = {}
products_ = get_products(products_)
print_total_price(products_)
