function addItem() {
    const listEl = document.querySelector('#items');
    const inputEl = document.querySelector('#newItemText');

    if (inputEl.value == '') return;

    const liElement = document.createElement('li');
    liElement.textContent = inputEl.value;
    listEl.appendChild(liElement);

    inputEl.value = '';
}
