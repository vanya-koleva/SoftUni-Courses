function solve() {
    const headRow = document.querySelector('table thead tr');
    const rows = document.querySelectorAll('table tbody tr');
    const outputEl = document.querySelector('#output');

    const checkedRows = [...headRow.children]
        .map((th, i) => ({
            el: th.children[0],
            name: th.children[0].getAttribute('name'),
            index: i,
        }))
        .filter(object => object.el.checked);

    const output = [...rows].map(row => {
        return checkedRows.reduce((acc, curr) => {
            acc[curr.name] = row.children[curr.index].textContent;
            return acc;
        }, {});
    });

    outputEl.value = JSON.stringify(output);
}
