function solve(array) {
    const newArray = [];
    const initialLength = array.length;

    array.sort((a, b) => a - b);

    for (let i = 0; i < initialLength; i++) {
        if (i % 2 === 0) {
            newArray.push(array.shift());
        } else {
            newArray.push(array.pop());
        }
    }

    return newArray;
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
