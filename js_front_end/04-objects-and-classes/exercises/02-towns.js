function solve(table) {
    const towns = [];

    for (const row of table) {
        const [town, latitude, longitude] = row.split(' | ');

        const entry = {
            town,
            latitude: Number(latitude).toFixed(2),
            longitude: Number(longitude).toFixed(2),
        };

        towns.push(entry);
    }

    towns.forEach(town => console.log(town));
}

function solve2(table) {
    table
        .map(row => row.split(' | '))
        .map(([town, latitude, longitude]) => ({
            town,
            latitude: Number(latitude).toFixed(2),
            longitude: Number(longitude).toFixed(2),
        }))
        .forEach(town => console.log(town));
}

solve2(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625']);
