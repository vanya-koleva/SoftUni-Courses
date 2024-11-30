function solve(product, quantity){
    let totalPrice = 0;
    const coffeePrice = 1.5;
    const waterPrice = 1;
    const cokePrice = 1.4;
    const snacksPrice = 2;

    switch (product) {
        case 'coffee':
            totalPrice = coffeePrice * quantity;
            break;
        case 'water':
            totalPrice = waterPrice * quantity;
            break;
        case 'coke':
            totalPrice = cokePrice * quantity;
            break;
        case 'snacks':
            totalPrice = snacksPrice * quantity;
            break;
    }
        
    console.log(`${totalPrice.toFixed(2)}`)
}

solve("water", 5);
solve("coffee", 2);
