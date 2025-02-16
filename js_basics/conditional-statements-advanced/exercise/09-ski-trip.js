function solve(days, accommodation, grade) {
    let price = 0;
    let nights = days - 1;

    if (accommodation === 'room for one person') {
        price = 18 * nights;
    } else if (accommodation === 'apartment') {
        price = 25 * nights;
        if (nights < 10) {
            price *= 0.7;
        } else if (nights > 15) {
            price *= 0.5;
        } else {
            price *= 0.65;
        }
    } else if (accommodation === 'president apartment') {
        price = 35 * nights;
        if (nights < 10) {
            price *= 0.9;
        } else if (nights > 15) {
            price *= 0.8;
        } else {
            price *= 0.85;
        }
    }

    if (grade === 'positive') {
        price *= 1.25;
    } else if (grade === 'negative') {
        price *= 0.9;
    }

    console.log(price.toFixed(2));
}

// solve(14, 'apartment', 'positive');
solve(30, 'president apartment', 'negative');

