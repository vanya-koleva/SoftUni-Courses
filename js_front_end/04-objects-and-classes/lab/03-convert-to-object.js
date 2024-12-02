function solve(input) {
    let info = JSON.parse(input);

    for (const key in info) {
        console.log(`${key}: ${info[key]}`);
    }
}

solve('{"name": "George", "age": 40, "town": "Sofia"}');
