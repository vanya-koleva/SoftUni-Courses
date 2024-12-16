function solve() {
    const num = Number(document.querySelector('#input').value);
    const convertTo = document.querySelector('#selectMenuTo').value.toLowerCase();
    const resultEl = document.querySelector('#result');

    switch (convertTo) {
        case 'binary':
            resultEl.value = num.toString(2);
            break;
        case 'hexadecimal':
            resultEl.value = num.toString(16).toUpperCase();
            break;
    }
}
