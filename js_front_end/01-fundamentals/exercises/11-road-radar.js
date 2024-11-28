function solve(speed, area) {
    switch (area) {
        case 'motorway':
            checkStatus(speed, 130);
            break;
        case 'interstate':
            checkStatus(speed, 90);
            break;
        case 'city':
            checkStatus(speed, 50);
            break;
        case 'residential':
            checkStatus(speed, 20);
            break;
    }

    function checkStatus(currentSpeed, speedLimit) {
        if (currentSpeed <= speedLimit) {
            console.log(`Driving ${currentSpeed} km/h in a ${speedLimit} zone`);
        } else {
            const difference = currentSpeed - speedLimit;
            let status;

            if (difference <= 20) {
                status = 'speeding';
            } else if (difference <= 40) {
                status = 'excessive speeding';
            } else {
                status = 'reckless driving';
            }

            console.log(
                `The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`
            );
        }
    }
}

solve(40, 'city');
solve(21, 'residential');
solve(120, 'interstate');
solve(200, 'motorway');
