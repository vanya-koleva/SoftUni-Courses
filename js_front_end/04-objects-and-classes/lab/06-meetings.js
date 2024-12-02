function solve(input) {
    const meetings = {};

    for (const entry of input) {
        const [day, person] = entry.split(' ');

        if (meetings[day]) {
            console.log(`Conflict on ${day}!`);
            continue;
        }

        meetings[day] = person;
        console.log(`Scheduled for ${day}`);
    }

    for (const day in meetings) {
        console.log(`${day} -> ${meetings[day]}`);
    }
}

solve(['Monday Peter', 'Wednesday Bill', 'Monday Tim', 'Friday Tim']);
