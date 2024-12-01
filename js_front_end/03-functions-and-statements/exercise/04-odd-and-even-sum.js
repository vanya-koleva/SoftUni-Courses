function oddAndEvenSum(number) {
    const evenSum = calculateSum(number, x => x % 2 === 0);
    const oddSum = calculateSum(number, x => x % 2 !== 0);

    printResult(oddSum, evenSum);

    function calculateSum(n, filter) {
        const filteredDigits = n.toString().split('').map(Number).filter(filter);

        const sum = filteredDigits.reduce((acc, digit) => acc + digit, 0);

        return sum;
    }

    function printResult(oddSum, evenSum) {
        console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
    }
}

oddAndEvenSum(1000435);
