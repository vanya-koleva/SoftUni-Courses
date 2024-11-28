function solve(fruit, weight, price) {
    const weightInKg = weight / 1000;
    const cost = price * weightInKg;
    console.log(`I need $${cost.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruit}.`);
}

solve('apple', 1563, 2.35);
solve('orange', 2500, 1.8);
