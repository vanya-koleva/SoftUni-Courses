function attachEvents() {
    const baseUrl = 'http://localhost:3030/jsonstore/messenger';
    
    const sendBtn = document.getElementById('submit');
    const refreshBtn = document.getElementById('refresh');
    const authorEl = document.querySelector('input[name="author"]');
    const contentEl = document.querySelector('input[name="content"]');
    const textareaEl = document.getElementById('messages');

    sendBtn.addEventListener('click', sendHandler);
    refreshBtn.addEventListener('click', refreshHandler);

    function sendHandler(e) {
        e.preventDefault();

        const author = authorEl.value.trim();
        const content = contentEl.value.trim();

        if (author === '' || content === '') return;

        fetch(baseUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ author, content })        
        })
        .then(res => res.json())
        .then(data => {
            authorEl.value = '';
            contentEl.value = '';
        })
        .catch(error => console.log('Error', error));
    }

    function refreshHandler(e) {
        e.preventDefault();

        fetch(baseUrl)
            .then(res => res.json())
            .then(data => {
                textareaEl.value = Object.values(data)
                    .map(({ author, content }) => `${author}: ${content}`)
                    .join('\n');
            })
            .catch(error => console.log('Error', error));
    }
}

attachEvents();
