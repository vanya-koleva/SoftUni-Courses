function solve(...input) {
    let budget = Number(input[0]);
    let season = input[1];
    let fishermenCount = Number(input[2]);
    
    let boatPrice = 0;
    if (season === "Spring") {
        boatPrice = 3000;
    } else if (season === "Summer" || season === "Autumn") {
        boatPrice = 4200;
    } else if (season === "Winter") {
        boatPrice = 2600;
    }

    if (fishermenCount <= 6) {
        boatPrice *= 0.9;
    } else if (fishermenCount <= 11) {
        boatPrice *= 0.85;
    } else {
        boatPrice *= 0.75;
    }

    if (fishermenCount % 2 === 0 && season !== "Autumn") {
        boatPrice *= 0.95;
    }

    let diff = Math.abs(budget - boatPrice);

    if (budget >= boatPrice) {
        console.log(`Yes! You have ${(diff).toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${(diff).toFixed(2)} leva.`);
    }
}

// solve(3000, "Summer", 11);
solve(3600, "Autumn", 6);
