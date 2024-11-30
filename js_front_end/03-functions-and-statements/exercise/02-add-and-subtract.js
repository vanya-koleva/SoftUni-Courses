function addAndSubtract(first, second, third) {
    const add = (a, b) => a + b;
    const subtract = (a, b) => a - b;

    const result = subtract(add(first, second), third);
    console.log(result);
}

addAndSubtract(23, 6, 10);
