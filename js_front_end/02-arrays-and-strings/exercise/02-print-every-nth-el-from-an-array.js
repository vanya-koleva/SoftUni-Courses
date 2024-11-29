function solve(array, step) {
    return array.filter(function (el, index) {
        return index % step === 0;
    });
}

console.log(solve(['5', '20', '31', '4', '20'], 2));
