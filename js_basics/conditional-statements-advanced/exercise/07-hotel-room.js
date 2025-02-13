function solve(month, nights) {
    nights = Number(nights);
    let studioPrice = 0;
    let apartmentPrice = 0;

    switch (month) {
        case 'May':
        case 'October':
            studioPrice = 50;
            apartmentPrice = 65;
            if (nights > 14) {
                studioPrice *= 0.7;
            } else if (nights > 7) {
                studioPrice *= 0.95;
            }
            break;
        case 'June':
        case 'September':
            studioPrice = 75.2;
            apartmentPrice = 68.7;
            if (nights > 14) {
                studioPrice *= 0.8;
            }
            break;
        case 'July':
        case 'August':
            studioPrice = 76;
            apartmentPrice = 77;
            break;
    }

    if (nights > 14) {
        apartmentPrice *= 0.9;
    }

    let studioTotalPrice = studioPrice * nights;
    let apartmentTotalPrice = apartmentPrice * nights;

    console.log(`Apartment: ${apartmentTotalPrice.toFixed(2)} lv.`);
    console.log(`Studio: ${studioTotalPrice.toFixed(2)} lv.`);
}

solve('May', 15);
solve('June', 14);

