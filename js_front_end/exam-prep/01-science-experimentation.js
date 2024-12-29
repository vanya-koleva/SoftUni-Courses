function solve(input) {
    const count = Number(input.shift());
    const chemicals = {};

    for (let i = 0; i < count; i++) {
        const [name, quantity] = input.shift().split(' # ');

        chemicals[name] = {
            name,
            quantity: Number(quantity),
        };
    }

    while (input[0] !== 'End') {
        const [command, ...args] = input.shift().split(' # ');

        switch (command) {
            case 'Mix':
                const [chem1, chem2, quantity] = args;
                mix(chem1, chem2, Number(quantity));
                break;
            case 'Replenish':
                const [chem, amount] = args;
                replenish(chem, Number(amount));
                break;
            case 'Add Formula':
                const [chemName, formula] = args;
                addFormula(chemName, formula);
                break;
        }
    }

    printChemicals();

    function mix(chem1, chem2, quantity) {
        if (chemicals[chem1].quantity < quantity || chemicals[chem2].quantity < quantity) {
            console.log(`Insufficient quantity of ${chem1}/${chem2} to mix.`);
        } else {
            chemicals[chem1].quantity -= quantity;
            chemicals[chem2].quantity -= quantity;
            console.log(`${chem1} and ${chem2} have been mixed. ${quantity} units of each were used.`);
        }
    }

    function replenish(chem, quantity) {
        if (chemicals[chem]) {
            if (chemicals[chem].quantity + quantity > 500) {
                const addedAmount = 500 - chemicals[chem].quantity;
                chemicals[chem].quantity = 500;
                console.log(
                    `${chem} quantity increased by ${addedAmount} units, reaching maximum capacity of 500 units!`
                );
            } else {
                chemicals[chem].quantity += quantity;
                console.log(`${chem} quantity increased by ${quantity} units!`);
            }
        } else {
            console.log(`The Chemical ${chem} is not available in the lab.`);
        }
    }

    function addFormula(chemName, formula) {
        if (!chemicals[chemName]) {
            console.log(`The Chemical ${chemName} is not available in the lab.`);
        } else {
            chemicals[chemName].formula = formula;
            console.log(`${chemName} has been assigned the formula ${formula}.`);
        }
    }

    function printChemicals() {
        for (const chemName in chemicals) {
            const chem = chemicals[chemName];
            console.log(
                `Chemical: ${chem.name}, Quantity: ${chem.quantity}${
                    chem.formula ? `, Formula: ${chem.formula}` : ''
                }`
            );
        }
    }
}

// solve([
//     '4',
//     'Water # 200',
//     'Salt # 100',
//     'Acid # 50',
//     'Base # 80',
//     'Mix # Water # Salt # 50',
//     'Replenish # Salt # 150',
//     'Add Formula # Acid # H2SO4',
//     'End',
// ]);

solve([
    '3',
    'Sodium # 300',
    'Chlorine # 100',
    'Hydrogen # 200',
    'Mix # Sodium # Chlorine # 200',
    'Replenish # Sodium # 250',
    'Add Formula # Sulfuric Acid # H2SO4',
    'Add Formula # Sodium # Na',
    'Mix # Hydrogen # Chlorine # 50',
    'End',
]);
