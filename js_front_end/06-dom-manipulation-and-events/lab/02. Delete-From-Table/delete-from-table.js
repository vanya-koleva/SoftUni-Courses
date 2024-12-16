function deleteByEmail() {
    const inputEl = document.querySelector('input[name="email"]');
    const resultElement = document.querySelector('#result');
    const tableEl = document.getElementById('customers');
    const tdElements = tableEl.querySelectorAll('tbody td:last-child');

    const searchEmail = inputEl.value;
    const searchEl = Array.from(tdElements).find(el => el.textContent === searchEmail);

    if (searchEl) {
        searchEl.parentElement.remove();
        resultElement.textContent = 'Deleted';
    } else {
        resultElement.textContent = 'Not found.';
    }
}
