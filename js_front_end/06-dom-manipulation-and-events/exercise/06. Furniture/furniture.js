document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const inputFormEl = document.getElementById('input');
    const inputEl = inputFormEl.querySelector('textarea');
    const shopFormEl = document.getElementById('shop');
    const outputEL = shopFormEl.querySelector('textarea');
    const productTable = shopFormEl.querySelector('table tbody');

    inputFormEl.addEventListener('submit', e => {
        e.preventDefault();

        const data = JSON.parse(inputEl.value);
        console.log(data);

        data.forEach(item => {
            const row = document.createElement('tr');

            const rowImageTd = document.createElement('td');
            const rowImageEl = document.createElement('img');
            rowImageEl.setAttribute('src', item.img);
            rowImageTd.append(rowImageEl);

            const rowNameTd = document.createElement('td');
            rowNameTd.textContent = item.name;

            const rowPriceTd = document.createElement('td');
            rowPriceTd.textContent = item.price;

            const rowDecTd = document.createElement('td');
            rowDecTd.textContent = item.decFactor;

            const rowCheckTd = document.createElement('td');
            const rowCheckInput = document.createElement('input');
            rowCheckInput.setAttribute('type', 'checkbox');
            rowCheckTd.append(rowCheckInput);

            row.append(rowImageTd, rowNameTd, rowPriceTd, rowDecTd, rowCheckTd);
            productTable.append(row);
        });
    });

    shopFormEl.addEventListener('submit', e => {
        e.preventDefault();

        let totalPrice = 0;
        let totalDecFactor = 0;
        let markedChildren = 0;
        let names = [];

        Array.from(productTable.children).forEach(trElement => {
            const markedEl = trElement.querySelector('input[type="checkbox"]');
            if (!markedEl.checked) return;

            const name = trElement.children[1].textContent;
            const price = Number(trElement.children[2].textContent);
            const decFactor = Number(trElement.children[3].textContent);

            names.push(name);
            totalPrice += price;
            totalDecFactor += decFactor;
            markedChildren++;
        });

        const avgDecFactor = totalDecFactor / markedChildren;
        outputEL.textContent = `Bought furniture: ${names.join(', ')}\n`;
        outputEL.textContent += `Total price: ${totalPrice}\n`;
        outputEL.textContent += `Average decoration factor: ${avgDecFactor}`;
    });
}
