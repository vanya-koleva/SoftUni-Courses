function solve(num1, num2, num3) {
    let result;
    if (num1 >= num2 && num1 >= num3) {
        result = num1;
    } else if (num2 >= num1 && num2 >= num3) {
        result = num2;
    } else {
        result = num3;
    }
    console.log(`The largest number is ${result}.`);
}
solve(5, -3, 16);
solve(-3, -5, -22.5);

function secondSolution(first, second, third) {
    let result = Math.max(first, second, third);
    console.log(`The largest number is ${result}.`);
}
