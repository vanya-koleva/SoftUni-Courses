function solve(numOfPeople, groupType, day) {
    const sFriday = 8.45;
    const sSaturday = 9.8;
    const sSunday = 10.46;

    const bFriday = 10.9;
    const bSaturday = 15.6;
    const bSunday = 16;

    const rFriday = 15;
    const rSaturday = 20;
    const rSunday = 22.5;

    let price;

    switch (groupType) {
        case 'Students':
            switch (day) {
                case 'Friday':
                    price = numOfPeople * sFriday;
                    break;
                case 'Saturday':
                    price = numOfPeople * sSaturday;
                    break;
                case 'Sunday':
                    price = numOfPeople * sSunday;
                    break;
            }

            if (numOfPeople >= 30) price *= 0.85;
            break;

        case 'Business':
            if (numOfPeople >= 100) numOfPeople -= 10;

            switch (day) {
                case 'Friday':
                    price = numOfPeople * bFriday;
                    break;
                case 'Saturday':
                    price = numOfPeople * bSaturday;
                    break;
                case 'Sunday':
                    price = numOfPeople * bSunday;
                    break;
            }
            break;

        case 'Regular':
            switch (day) {
                case 'Friday':
                    price = numOfPeople * rFriday;
                    break;
                case 'Saturday':
                    price = numOfPeople * rSaturday;
                    break;
                case 'Sunday':
                    price = numOfPeople * rSunday;
                    break;
            }

            if (numOfPeople >= 10 && numOfPeople <= 20) price *= 0.95;
            break;
    }

    console.log(`Total price: ${price.toFixed(2)}`);
}

solve(40, 'Regular', 'Saturday');
