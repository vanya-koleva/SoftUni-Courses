function calculateProfit(input) {
    let showType = input[0];
    let rows = Number(input[1]);
    let columns = Number(input[2]);
    let price = 0;

    switch(showType) {
        case "Premiere":
            price = 12;
            break;
        case "Normal":
            price = 7.5;
            break;
        default:
            price = 5;
            break;
    }

    let totalPrice = rows * columns * price
    console.log(`${totalPrice.toFixed(2)} leva`)
}

calculateProfit(["Discount", "12", "30"])
