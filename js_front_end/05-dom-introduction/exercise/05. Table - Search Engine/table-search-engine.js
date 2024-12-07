function solve() {
    const rows = document.querySelectorAll('table tbody tr');
    const searchStr = document.querySelector('#searchField').value.toLowerCase().trim();

    if (searchStr === '') return;

    rows.forEach(row => {
        row.classList.remove('select');

        if (row.textContent.toLowerCase().includes(searchStr)) {
            row.classList.add('select');
        }
    });
}
