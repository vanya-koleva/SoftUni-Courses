function solve(...input) {
    let flowersType = input[0];
    let flowersCount = Number(input[1]);
    let budget = Number(input[2]);

    let rosePrice = 5;
    let dahliasPrice = 3.8;
    let tulipsPrice = 2.8;
    let narcissusPrice = 3;
    let gladiolusPrice = 2.5;

    let totalPrice = 0;

    switch (flowersType) {
        case 'Roses':
            totalPrice = rosePrice * flowersCount;
            if (flowersCount > 80) {
                totalPrice *= 0.9;
            }
            break;
        case 'Dahlias':
            totalPrice = dahliasPrice * flowersCount;
            if (flowersCount > 90) {
                totalPrice *= 0.85;
            }
            break;
        case 'Tulips':
            totalPrice = tulipsPrice * flowersCount;
            if (flowersCount > 80) {
                totalPrice *= 0.85;
            }
            break;
        case 'Narcissus':
            totalPrice = narcissusPrice * flowersCount;
            if (flowersCount < 120) {
                totalPrice *= 1.15;
            }
            break;
        case 'Gladiolus':
            totalPrice = gladiolusPrice * flowersCount;
            if (flowersCount < 80) {
                totalPrice *= 1.2;
            }
            break;
    }

    remainingMoney = Math.abs(budget - totalPrice);

    if (budget >= totalPrice) {
        console.log(
            `Hey, you have a great garden with ${flowersCount} ${flowersType} and ${remainingMoney.toFixed(
                2
            )} leva left.`
        );
    } else {
        console.log(`Not enough money, you need ${remainingMoney.toFixed(2)} leva more.`);
    }
}

// solve("Roses", 55, 250);
// solve('Tulips', 88, 260);
solve('Narcissus', 119, 360);
