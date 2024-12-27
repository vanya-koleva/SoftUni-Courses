function lockedProfile() {
    const baseURL = 'http://localhost:3030/jsonstore/advanced/profiles';

    const mainEl = document.querySelector('main');
    const template = document.querySelector('.profile');

    function loadProfiles() {
        fetch(baseURL)
            .then(res => res.json())
            .then(data => {
                template.remove();

                Object.values(data).forEach(profile => {
                    const cloneEl = template.cloneNode(true);
                    cloneEl.querySelector('input[name="user1Username"]').value = profile.username;
                    cloneEl.querySelector('input[name="user1Email"]').value = profile.email;
                    cloneEl.querySelector('input[name="user1Age"]').value = profile.age;
                    cloneEl.querySelector('input[value="lock"]').checked = true;
                    cloneEl.querySelector('div.user1Username').style.display = 'none';
                    cloneEl.querySelector('button').textContent = 'Show more';

                    cloneEl.querySelector('button').addEventListener('click', lockHandler);

                    mainEl.appendChild(cloneEl);
                });
            })
            .catch(err => console.log(err));
    }

    function lockHandler(e) {
        const profile = e.target.parentElement.parentElement;
        const details = profile.querySelector('div.user1Username');
        const button = profile.querySelector('button');
        const locked = profile.querySelector('input[value="lock"]').checked;

        if (!locked) {
            if (details.style.display === 'none') {
                details.style.display = 'block';
                button.textContent = 'Hide it';
            } else {
                details.style.display = 'none';
                button.textContent = 'Show more';
            }
        }
    }

    loadProfiles();
}
