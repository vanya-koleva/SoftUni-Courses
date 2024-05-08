function calculateExpenses(input) {
    let budget = Number(input[0]);
    let statistsCount = Number(input[1]);
    let clothingPrice = Number(input[2]);

    let decorPrice = budget * 0.10
    let totalClothingPrice = statistsCount * clothingPrice
    if (statistsCount > 150) {
        totalClothingPrice *= 0.90
    }
    let totalPrice = totalClothingPrice + decorPrice
    let diff = Math.abs(totalPrice - budget)

    if (budget >= totalPrice) {
        console.log("Action!")
        console.log(`Wingard starts filming with ${diff.toFixed(2)} leva left.`)
    } else {
        console.log("Not enough money!")
        console.log(`Wingard needs ${diff.toFixed(2)} leva more.`)
    }
}

calculateExpenses(["9587.88", "222", "55.68"])
