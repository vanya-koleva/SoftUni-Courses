function calculateExpenses(input) {
    let budget = Number(input[0]);
    let videoCardsCount = Number(input[1]);
    let processorsCount = Number(input[2]);
    let ramCount = Number(input[3]);

    let videoCardsPrice = 250 * videoCardsCount;
    let processorsPrice = videoCardsPrice * 0.35 * processorsCount;
    let ramPrice = videoCardsPrice * 0.10 * ramCount;
    let totalPrice = videoCardsPrice + processorsPrice + ramPrice;

    if (videoCardsCount > processorsCount) {
        totalPrice = totalPrice * 0.85;
    }

    let diff = Math.abs(budget - totalPrice);

    if (budget >= totalPrice) {
        console.log(`You have ${diff.toFixed(2)} leva left!`)
    } else {
        console.log(`Not enough money! You need ${diff.toFixed(2)} leva more!`)
    }
}

calculateExpenses(["920.45", "3", "1", "1"])
