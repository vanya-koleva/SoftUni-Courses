function solve(input) {
    input
        .map(raw => raw.split(' / '))
        .map(([name, level, items]) => ({
            name,
            items,
            level: Number(level),
        }))
        .sort((a, b) => a.level - b.level)
        .forEach(hero => {
            console.log(`Hero: ${hero.name}`);
            console.log(`level => ${hero.level}`);
            console.log(`items => ${hero.items}`);
        });
}

solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara',
]);
