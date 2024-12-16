function addItem() {
    function deleteItem(e) {
        e.currentTarget.parentElement.remove();
    }

    const listEl = document.querySelector('#items');
    const inputEl = document.querySelector('#newItemText');

    const newListItem = document.createElement('li');
    const deleteButton = document.createElement('a');

    newListItem.textContent = inputEl.value;
    deleteButton.setAttribute('href', '#');
    deleteButton.textContent = '[Delete]';

    deleteButton.addEventListener('click', deleteItem);

    newListItem.appendChild(deleteButton);
    listEl.appendChild(newListItem);

    inputEl.value = '';
}
