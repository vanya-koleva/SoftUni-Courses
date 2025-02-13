function solve(examHour, examMinute, arrivalHour, arrivalMinute) {
    let timeOfExam = examHour * 60 + examMinute;
    let timeOfArrival = arrivalHour * 60 + arrivalMinute;
    let difference = Math.abs(timeOfExam - timeOfArrival);
    let hours = Math.floor(difference / 60);
    let minutes = difference % 60;

    if (timeOfArrival > timeOfExam) {
        console.log('Late');

        if (difference < 60) {
            console.log(`${minutes} minutes after the start`);
        } else {
            if (minutes < 10) {
                console.log(`${hours}:0${minutes} hours after the start`);
            } else {
                console.log(`${hours}:${minutes} hours after the start`);
            }
        }
    } else if (difference <= 30) {
        console.log('On time');

        if (difference > 0) {
            console.log(`${minutes} minutes before  the start`);
        }
    } else {
        console.log('Early');

        if (difference < 60) {
            console.log(`${minutes} minutes before the start`);
        } else {
            if (minutes < 10) {
                console.log(`${hours}:0${minutes} hours before the start`);
            } else {
                console.log(`${hours}:${minutes} hours before the start`);
            }
        }
    }
}

solve(9, 30, 9, 50);

