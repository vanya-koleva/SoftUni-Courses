function attachGradientEvents() {
    const gradientEl = document.querySelector('#gradient');
    const resultEl = document.querySelector('#result');

    gradientEl.addEventListener('mousemove', e => {
        const currentPos = e.offsetX;
        const elementWidtch = e.currentTarget.clientWidth;
        const percent = Math.floor((currentPos / elementWidtch) * 100);

        resultEl.textContent = percent + '%';
    });
}
