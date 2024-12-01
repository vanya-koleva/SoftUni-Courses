function solve(num1, num2) {
    function calculateFactorial(num) {
        if (num <= 1) {
            return 1;
        }

        return num * calculateFactorial(num - 1);
    }

    const result = calculateFactorial(num1) / calculateFactorial(num2);

    console.log(result.toFixed(2));
}

solve(5, 2);
solve(6, 2);
