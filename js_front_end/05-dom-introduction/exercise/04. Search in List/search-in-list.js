function solve() {
    const towns = document.querySelectorAll('#towns li');
    const input = document.querySelector('#searchText').value.toLowerCase();
    const resultEl = document.querySelector('#result');

    if (input === '') return;

    towns.forEach(town => {
        town.classList.remove('match');
        town.style.fontWeight = 'normal';
        town.style.textDecoration = 'none';

        if (town.textContent.toLowerCase().includes(input)) {
            town.classList.add('match');
            town.style.fontWeight = 'bold';
            town.style.textDecoration = 'underline';
        }
    });

    resultEl.textContent = `${document.querySelectorAll('.match').length} matches found`;
}
