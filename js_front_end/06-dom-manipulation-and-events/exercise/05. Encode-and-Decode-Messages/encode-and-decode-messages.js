document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const encodeFormEl = document.querySelector('#encode');
    const encodeTextEl = encodeFormEl.querySelector('textarea');
    const decodeFormEl = document.querySelector('#decode');
    const decodeTextEl = decodeFormEl.querySelector('textarea');

    function handleEncode(e) {
        e.preventDefault();

        const message = encodeTextEl.value;

        let encodedMessage = [];

        for (let i = 0; i < message.length; i++) {
            const newAsciiCode = message.charCodeAt(i) + 1;
            encodedMessage.push(String.fromCharCode(newAsciiCode));
        }

        // const encodedMessage = message.split('').map(ch => String.fromCharCode( ch.charCodeAt() + 1 ) ).join('');

        encodeTextEl.value = '';
        decodeTextEl.value = encodedMessage.join('');
    }

    function handleDecode(e) {
        e.preventDefault();

        const message = decodeTextEl.value;
        let decodedMessage = [];

        for (let i = 0; i < message.length; i++) {
            const newAsciiCode = message.charCodeAt(i) - 1;
            decodedMessage.push(String.fromCharCode(newAsciiCode));
        }

        encodeTextEl.value = '';
        decodeTextEl.value = decodedMessage.join('');
    }

    encodeFormEl.addEventListener('click', handleEncode);
    decodeFormEl.addEventListener('click', handleDecode);
}
