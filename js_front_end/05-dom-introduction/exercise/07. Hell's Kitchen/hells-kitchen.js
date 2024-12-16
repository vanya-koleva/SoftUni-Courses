function solve() {
    const input = document.querySelector('#inputs textarea').value;
    const bestRestEl = document.querySelector('#bestRestaurant p');
    const bestWorkersEl = document.querySelector('#workers p');

    if (!input) return;

    const restaurants = JSON.parse(input).reduce((acc, curr) => {
        const [name, workersData] = curr.split(' - ');
        const workers = workersData.split(', ').map(workerData => {
            const [name, salary] = workerData.split(' ');
            return { name, salary: Number(salary) };
        });

        acc[name] ??= { workers: [] };
        acc[name].workers.push(...workers);

        return acc;
    }, {});

    function getAvgSalary(restaurant) {
        const allSalaries = restaurant.workers.reduce((acc, w) => acc + w.salary, 0);
        return allSalaries / restaurant.workers.length;
    }

    const [bestRestKey] = Object.keys(restaurants).sort(
        (a, b) => getAvgSalary(restaurants[b]) - getAvgSalary(restaurants[a])
    );

    const bestWorkers = restaurants[bestRestKey].workers.toSorted((a, b) => b.salary - a.salary);

    bestRestEl.textContent = `Name: ${bestRestKey} `;
    bestRestEl.textContent += `Average Salary: ${getAvgSalary(restaurants[bestRestKey]).toFixed(2)} `;
    bestRestEl.textContent += `Best Salary: ${bestWorkers[0].salary.toFixed(2)}`;

    bestWorkersEl.textContent = bestWorkers.map(w => `Name: ${w.name} With Salary: ${w.salary}`).join(' ');
}
