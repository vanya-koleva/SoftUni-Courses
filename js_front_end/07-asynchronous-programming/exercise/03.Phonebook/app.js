function attachEvents() {
    const baseUrl = 'http://localhost:3030/jsonstore/phonebook';

    const loadBtn = document.getElementById('btnLoad');
    const phonebookEl = document.getElementById('phonebook');
    const createBtn = document.getElementById('btnCreate');
    const personEl = document.getElementById('person');
    const phoneEl = document.getElementById('phone');

    loadBtn.addEventListener('click', loadHandler);
    createBtn.addEventListener('click', createHandler);


    function loadHandler(e) {
        phonebookEl.innerHTML = '';

        fetch(baseUrl)
            .then(res => res.json())
            .then(data => {
                Object.entries(data).forEach(([key, entry]) => {
                    const li = document.createElement('li');
                    li.textContent = `${entry.person}: ${entry.phone}`;
                    li.dataset.id = key;

                    const button = document.createElement('button');
                    button.textContent = 'Delete';
                    button.addEventListener('click', (e) => {
                        fetch(`${baseUrl}/${key}`, {
                            method: 'DELETE'
                        })
                            .then(() => {
                                e.target.parentElement.remove();
                            });
                    });

                    li.appendChild(button);
                    phonebookEl.appendChild(li);
                })
                
                console.log(phonebookEl);
            })
            .catch(error => console.log('Error', error));
    }

    function createHandler(e) {
        fetch(baseUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                person: personEl.value, 
                phone: phoneEl.value, 
            })
        })
            .then(res => res.json())
            .then(() => {
                personEl.value = '';
                phoneEl.value = '';
                loadHandler();
            })
            .catch(error => console.log('Error', error));
    }
}

attachEvents();
