document.addEventListener('DOMContentLoaded', solve);

function solve() {
    function sectionFocusedHandler(e) {
        e.currentTarget.parentElement.classList.add('focused');
    }

    function sectionBlurHandler(e) {
        e.currentTarget.parentElement.classList.remove('focused');
    }

    const inputElements = document.querySelectorAll('input[type="text"]');

    [...inputElements].forEach(el => {
        el.addEventListener('focus', sectionFocusedHandler);
        el.addEventListener('blur', sectionBlurHandler);
    });
}

// function solve() {
//     const sections = Array.from(document.querySelectorAll('.panel'));

//     sections.forEach(section => {
//         const inputEl = section.querySelector('input');
//         inputEl.addEventListener('focus', () => {
//             section.classList.add('focused');
//         });
//         inputEl.addEventListener('blur', () => {
//             section.classList.remove('focused');
//         });
//     });
// }
