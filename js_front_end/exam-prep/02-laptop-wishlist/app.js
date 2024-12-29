window.addEventListener('load', solve);

function solve() {
    const formEl = document.querySelector('.laptop-info');
    const modelEl = document.querySelector('#laptop-model');
    const storageEl = document.querySelector('#storage');
    const priceEl = document.querySelector('#price');
    const addBtn = document.querySelector('#add-btn');
    const checklistEl = document.querySelector('#check-list');
    const laptopsListEl = document.querySelector('#laptops-list');
    const clearBtn = document.querySelector('button.clear');

    addBtn.addEventListener('click', addHandler);
    clearBtn.addEventListener('click', clearHandler);

    function clearHandler(e) {
        location.reload();
    }

    function addHandler(e) {
        e.preventDefault();

        let model = modelEl.value;
        let storage = storageEl.value;
        let price = priceEl.value;

        if (model === '' || storage === '' || price === '') return;

        const liEl = document.createElement('li');
        liEl.classList.add('laptop-item');

        const articleEl = document.createElement('article');

        const newPEl = document.createElement('p');
        newPEl.textContent = model;

        const newPEl2 = document.createElement('p');
        newPEl2.textContent = `Memory: ${storage} TB`;

        const newPEl3 = document.createElement('p');
        newPEl3.textContent = `Price: ${price}$`;

        articleEl.appendChild(newPEl);
        articleEl.appendChild(newPEl2);
        articleEl.appendChild(newPEl3);

        liEl.appendChild(articleEl);

        const editBtn = document.createElement('button');
        editBtn.classList.add('btn');
        editBtn.classList.add('edit');
        editBtn.textContent = 'edit';
        editBtn.addEventListener('click', editHandler);

        const okBtn = document.createElement('button');
        okBtn.classList.add('btn');
        okBtn.classList.add('ok');
        okBtn.textContent = 'ok';
        okBtn.addEventListener('click', okHandler);

        liEl.appendChild(editBtn);
        liEl.appendChild(okBtn);

        checklistEl.appendChild(liEl);

        formEl.reset();
        addBtn.disabled = true;

        function editHandler(e) {
            modelEl.value = model;
            storageEl.value = storage;
            priceEl.value = price;

            checklistEl.removeChild(liEl);
            addBtn.disabled = false;
        }

        function okHandler(e) {
            liEl.removeChild(editBtn);
            liEl.removeChild(okBtn);
            laptopsListEl.appendChild(liEl);

            addBtn.disabled = false;
        }
    }
}
