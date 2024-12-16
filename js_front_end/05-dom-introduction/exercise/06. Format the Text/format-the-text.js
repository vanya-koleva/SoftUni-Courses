function solve() {
    const sentences = document.querySelector('#input').value.split('. ');
    const resultEl = document.querySelector('#output');

    const sentPerPar = 3;
    const numOfPar = Math.ceil(sentences.length / sentPerPar);

    let output = '';

    for (let i = 0; i < numOfPar; i++) {
        const start = i * sentPerPar;
        const end = start + sentPerPar;

        output += '<p>';
        output += sentences.slice(start, end).join('. ');
        output += '</p>';
    }

    resultEl.innerHTML = output;
}
