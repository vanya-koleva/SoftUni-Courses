function attachEvents() {
    const postsURL = 'http://localhost:3030/jsonstore/blog/posts';
    const commentsURL = 'http://localhost:3030/jsonstore/blog/comments';

    const loadBtn = document.getElementById('btnLoadPosts');
    const postsEl = document.getElementById('posts');
    const viewPostBtn = document.getElementById('btnViewPost');
    const postTitleEl = document.getElementById('post-title');
    const postBodyEl = document.getElementById('post-body');
    const commentsEl = document.getElementById('post-comments');

    loadBtn.addEventListener('click', loadHandler);
    viewPostBtn.addEventListener('click', viewPostHandler);

    function loadHandler(e) {
        fetch(postsURL)
            .then(res => res.json())
            .then(posts=> {
                Object.values(posts)
                    .forEach(post => {
                        const optionEl = document.createElement('option');
                        Object.assign(optionEl.dataset, post);
                        optionEl.textContent = post.title;

                        postsEl.appendChild(optionEl);
                    });
            })
            .catch(error => console.log('Error', error));
    }

    function viewPostHandler(e) {
        fetch(commentsURL)
            .then(res => res.json())
            .then(comments => {
                const selectedEl = postsEl.querySelector('option:checked');

                postTitleEl.textContent = selectedEl.dataset.title;
                postBodyEl.textContent = selectedEl.dataset.body;

                Object.values(comments)
                    .forEach(comment => {
                        if (comment.postId === selectedEl.dataset.id) {
                            const liEl = document.createElement('li');
                            liEl.textContent = comment.text;
                            commentsEl.appendChild(liEl);
                        }
                    });
            })
            .catch(error => console.log('Error', error));
    }
}

attachEvents();
