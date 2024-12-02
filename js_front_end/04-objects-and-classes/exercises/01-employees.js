function solve(input) {
    const employees = [];

    for (const entry of input) {
        const employee = {
            name: entry,
            personalNum: entry.length,
        };

        employees.push(employee);
    }

    employees.forEach(employee =>
        console.log(`Name: ${employee.name} -- Personal Number: ${employee.personalNum}`)
    );
}

function solve2(employeeNames) {
    employeeNames
        .map(name => ({
            name,
            personalNum: name.length,
        }))
        .forEach(employee =>
            console.log(`Name: ${employee.name} -- Personal Number: ${employee.personalNum}`)
        );
}

solve2(['Silas Butler', 'Adnaan Buckley', 'Juan Peterson', 'Brendan Villarreal']);
