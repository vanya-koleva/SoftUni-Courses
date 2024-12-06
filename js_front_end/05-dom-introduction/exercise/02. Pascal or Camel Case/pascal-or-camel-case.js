function solve() {
    const text = document.querySelector('#text').value.toLowerCase().split(' ');
    const convention = document.querySelector('#naming-convention').value.toLowerCase().trim();
    const resultEl = document.querySelector('#result');

    function capitalizeWord(word) {
        return word[0].toUpperCase() + word.slice(1);
    }

    switch (convention) {
        case 'camel case':
            resultEl.textContent = text[0] + text.slice(1).map(capitalizeWord).join('');
            break;
        case 'pascal case':
            resultEl.textContent = text.map(capitalizeWord).join('');
            break;
        default:
            resultEl.textContent = 'Error!';
    }
}
