function solve(stock, deliveries) {
    const getProducts = array => {
        const products = {};

        for (let i = 0; i < array.length; i += 2) {
            const product = array[i];
            const quantity = Number(array[i + 1]);

            if (!products[product]) {
                products[product] = 0;
            }

            products[product] += quantity;
        }

        return products;
    };

    const store = getProducts([...stock, ...deliveries]);

    for (const product in store) {
        console.log(`${product} -> ${store[product]}`);
    }
}

solve(
    ['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],
    ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']
);
