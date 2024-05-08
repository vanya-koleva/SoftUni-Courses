function calculateProfit(input) {
    let excursionPrice = Number(input[0]);
    let puzzlesCount = Number(input[1]);
    let dollsCount = Number(input[2]);
    let bearsCount = Number(input[3]);
    let minionsCount = Number(input[4]);
    let trucksCount = Number(input[5]);

    let puzzlePrice = 2.60;
    let dollPrice = 3;
    let bearPrice = 4.10;
    let minionPrice = 8.20;
    let truckPrice = 2;

    let totalToysCount = puzzlesCount + dollsCount + bearsCount + minionsCount + trucksCount;
    let totalMoney = puzzlesCount * puzzlePrice + dollsCount * dollPrice + bearsCount * bearPrice + minionsCount * minionPrice + trucksCount * truckPrice;

    if (totalToysCount >= 50) {
        totalMoney *= 0.75;
    }

    totalMoney *= 0.90;

    if (totalMoney >= excursionPrice) {
        console.log(`Yes! ${(totalMoney - excursionPrice).toFixed(2)} lv left.`);
    } else {
        console.log(`Not enough money! ${(excursionPrice - totalMoney).toFixed(2)} lv needed.`);
    }
}

calculateProfit(["320", "8", "2", "5", "5", "1"])
