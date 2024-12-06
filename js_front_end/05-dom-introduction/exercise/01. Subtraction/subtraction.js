function subtract() {
    const num1 = Number(document.querySelector('#firstNumber').value);
    const num2 = Number(document.querySelector('#secondNumber').value);
    const resultEl = document.querySelector('#result');

    resultEl.textContent = num1 - num2;
}
