function solve(firstName, lastName, hairColor) {
    let info = {
        name: firstName,
        lastName,
        hairColor,
    };

    console.log(JSON.stringify(info));
}

solve('George', 'Jones', 'Brown');
