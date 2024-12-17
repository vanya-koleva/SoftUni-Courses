document.addEventListener('DOMContentLoaded', solve);

function solve() {
    document.querySelector('main').addEventListener('click', e => {
        if (e.target.nodeName !== 'BUTTON') return;

        const profileEl = e.target.closest('.profile');
        const state = profileEl.querySelector('.radio-group input:checked').getAttribute('id');

        console.log(state);

        if (state.includes('Lock')) return;

        const hiddenFieldsEl = profileEl.querySelector('.hidden-fields');

        if (hiddenFieldsEl.classList.contains('active')) {
            hiddenFieldsEl.classList.remove('active');
            e.target.textContent = 'Show less';
        } else {
            hiddenFieldsEl.classList.add('active');
            e.target.textContent = 'Show more';
        }
    });
}
