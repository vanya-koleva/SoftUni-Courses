function solve(...input) {
    let num1 = Number(input[0]);
    let num2 = Number(input[1]);
    let operator = input[2];

    let result = 0;
    if (operator === '+') {
        result = num1 + num2;
    } else if (operator === '-') {
        result = num1 - num2;
    } else if (operator === '*') {
        result = num1 * num2;
    } else if (operator === '/') {
        if (num2 === 0) {
            console.log(`Cannot divide ${num1} by zero`);
            return;
        }
        result = num1 / num2;
    } else if (operator === '%') {
        if (num2 === 0) {
            console.log(`Cannot divide ${num1} by zero`);
            return;
        }
        result = num1 % num2;
    }

    if (operator === '+' || operator === '-' || operator === '*') {
        console.log(
            `${num1} ${operator} ${num2} = ${result} - ${
                result % 2 === 0 ? 'even' : 'odd'
            }`
        );
    } else if (operator === '/') {
        console.log(`${num1} ${operator} ${num2} = ${result.toFixed(2)}`);
    } else {
        console.log(`${num1} ${operator} ${num2} = ${result}`);
    }
}

solve(10, 12, '+');
solve(10, 1, '-');
solve(123, 12, '/');
solve(10, 3, '%');
solve(112, 0, '/');

