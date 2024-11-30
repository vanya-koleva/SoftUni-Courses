function solve(...numbers) {
    negativeNums = numbers.filter(num => num < 0);

    if (negativeNums.length % 2 === 1) {
        console.log('Negative');
    } else {
        console.log('Positive');
    }
}

solve(5, 12, -15);
solve(-6, -12, 14);
solve(-1, -2, -3);
solve(-5, 1, 1);
