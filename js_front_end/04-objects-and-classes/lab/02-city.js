function solve(input) {
    for (const key in input) {
        console.log(`${key} -> ${input[key]}`);
    }
}

function solve2(input) {
    const keys = Object.keys(input);

    for (const key of keys) {
        console.log(`${key} -> ${input[key]}`);
    }
}

function solve3(input) {
    const entries = Object.entries(input);

    for (const [key, value] of entries) {
        console.log(`${key} -> ${value}`);
    }
}

solve({
    name: 'Sofia',
    area: 492,
    population: 1238438,
    country: 'Bulgaria',
    postCode: '1000',
});

solve2({
    name: 'Plovdiv',
    area: 389,
    population: 1162358,
    country: 'Bulgaria',
    postCode: '4000',
});
