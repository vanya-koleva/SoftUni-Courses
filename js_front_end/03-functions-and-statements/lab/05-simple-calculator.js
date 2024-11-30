function solve(num1, num2, operation) {
    let operate = null;

    switch (operation) {
        case 'multiply':
            operate = (a, b) => a * b;
            break;
        case 'divide':
            operate = (a, b) => a / b;
            break;
        case 'add':
            operate = (a, b) => a + b;
            break;
        case 'subtract':
            operate = (a, b) => a - b;
            break;
    }

    const result = operate(num1, num2);

    console.log(result);
}

solve(5, 5, 'multiply');
solve(40, 8, 'divide');
solve(12, 19, 'add');
solve(50, 13, 'subtract');
