function solve(num) {
    let argType = typeof num;
    if (argType !== 'number') {
        console.log(`We can not calculate the circle area, because we receive a ${argType}.`);
    } else {
        let circleArea = Math.PI * num ** 2;
        console.log(circleArea.toFixed(2));
    }
}

solve(5);
solve('a');
