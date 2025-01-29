function solve(budget, season) {
    budget = Number(budget);
    let destination = '';
    let price = 0;
    let accommodation = ''

    if (budget <= 100) {
        destination = 'Bulgaria';
        if (season === 'summer') {
            price = budget * 0.3;
        } else {
            price = budget * 0.7
        }

    } else if (budget <= 1000) {
        destination = 'Balkans'
        if (season === 'summer') {
            price = budget * 0.4;
        } else {
            price = budget * 0.8
        }

    } else {
        destination = 'Europe'
        price = budget * 0.9
        accommodation = 'Hotel'
    }

    if (destination != 'Europe') {
        if (season === 'summer') {
            accommodation = 'Camp'
        } else {
            accommodation = 'Hotel'
        }
    }

    console.log(`Somewhere in ${destination}`);
    console.log(`${accommodation} - ${price.toFixed(2)}`)
}

// solve(50, "summer");
// solve(75, "winter");
// solve(312, "summer");
// solve(678.53, "winter");
solve(1500, "summer");
