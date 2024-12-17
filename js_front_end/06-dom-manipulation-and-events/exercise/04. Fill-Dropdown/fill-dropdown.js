document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const newItemTextEl = document.querySelector('#newItemText');
    const newItemValueEl = document.querySelector('#newItemValue');
    const menuEl = document.querySelector('#menu');

    document.querySelector('form').addEventListener('submit', handleSubmitEvent);

    function handleSubmitEvent(e) {
        e.preventDefault();
        const optionEl = document.createElement('option');

        optionEl.textContent = newItemTextEl.value;
        optionEl.value = newItemValueEl.value;

        menuEl.appendChild(optionEl);
        newItemTextEl.value = '';
        newItemValueEl.value = '';
    }
}
