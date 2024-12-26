function attachEvents() {
    const baseUrl = 'http://localhost:3030/jsonstore/collections/students';

    const submitBtn = document.getElementById('submit');
    const inputEls = document.querySelectorAll('input[type="text"]');
    const tableEl = document.querySelector('table tbody');

    submitBtn.addEventListener('click', submitHandler);

    function submitHandler(e) {
        e.preventDefault();

        const [firstName, lastName, facultyNumber, grade] = [...inputEls].map(el => el.value);

        if (!firstName || !lastName || !facultyNumber || !grade) return;

        const student = {
            firstName,
            lastName,
            facultyNumber,
            grade,
        };

        fetch(baseUrl, {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(student),
        })
            .then(res => res.json())
            .then(data => {
                const row = createRow(data);
                tableEl.appendChild(row);

                inputEls.forEach(el => (el.value = ''));
            })
            .catch(err => console.log(err));
    }

    function createRow(data) {
        const trEl = document.createElement('tr');

        const createTdEl = value => {
            const tdEl = document.createElement('td');
            tdEl.textContent = value;
            return tdEl;
        };

        trEl.appendChild(createTdEl(data.firstName));
        trEl.appendChild(createTdEl(data.lastName));
        trEl.appendChild(createTdEl(data.facultyNumber));
        trEl.appendChild(createTdEl(data.grade));

        return trEl;
    }

    fetch(baseUrl)
        .then(res => res.json())
        .then(data => {
            Object.values(data).forEach(student => {
                const row = createRow(student);
                tableEl.appendChild(row);
            });
        })
        .catch(err => console.log(err));
}

attachEvents();
