document.addEventListener('DOMContentLoaded', solution);

function solution() {
    const baseUrl = 'http://localhost:3030/jsonstore/advanced/articles';

    const mainEl = document.querySelector('#main');
    const template = document.querySelector('.accordion');

    function loadArticles() {
        fetch(`${baseUrl}/list`)
            .then(res => res.json())
            .then(data => {
                template.remove();

                Object.values(data).forEach(article => {
                    const cloneEl = template.cloneNode(true);
                    cloneEl.querySelector('span').textContent = article.title;
                    cloneEl.querySelector('button').setAttribute('id', article._id);

                    cloneEl.querySelector('button').addEventListener('click', contentHandler);

                    mainEl.appendChild(cloneEl);
                });
            })
            .catch(err => console.log(err));
    }

    function contentHandler(e) {
        const button = e.target;
        const contentEl = button.closest('.accordion').querySelector('div.extra');

        fetch(`${baseUrl}/details/${button.id}`)
            .then(res => res.json())
            .then(data => {
                if (button.textContent === 'More') {
                    contentEl.querySelector('p').textContent = data.content;
                    contentEl.style.display = 'block';
                    button.textContent = 'Hide it';
                } else {
                    contentEl.style.display = 'none';
                    button.textContent = 'More';
                }
            });
    }

    loadArticles();
}
