function perfectNumber(number) {
    const calculateSum = numbers => numbers.reduce((a, b) => a + b, 0);
    const isPerfect = number => calculateSum(getDivisors(number)) === number;

    if (isPerfect(number)) {
        console.log('We have a perfect number!');
    } else {
        console.log("It's not so perfect.");
    }

    function getDivisors(num) {
        const divisors = [];

        for (let i = Math.floor(num / 2); i > 0; i--) {
            if (num % i === 0) {
                divisors.push(i);
            }
        }

        return divisors;
    }
}

perfectNumber(6);
perfectNumber(28);
perfectNumber(1236498);
